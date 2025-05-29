import pandas as pd
import duckdb
import random
import re
from pathlib import Path


# source URL for FRED industrial production data
INDPRO_URL = (
    "https://fred.stlouisfed.org/graph/fredgraph.csv?"
    "bgcolor=%23ebf3fb&chart_type=line&drp=0&fo=open%20sans&"
    "graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&"
    "txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&"
    "show_legend=yes&show_axis_titles=yes&show_tooltip=yes&"
    "id=INDPRO&scale=left&cosd=1919-01-01&coed=2025-03-01&"
    "line_color=%230073e6&link_values=false&line_style=solid&"
    "mark_type=none&mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&"
    "fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&"
    "transformation=lin&vintage_date=2025-05-13&revision_date=2025-05-13&nd=1919-01-01"
)

def fetch_indpro_data(
    url: str = INDPRO_URL,
    start_date: str = "2010-01-01",
    end_date: str = "2020-12-31",
    output_path: str = "../data/raw/INDPRO.csv"
) -> pd.DataFrame:
    """
    Download the INDPRO series from FRED, filter to a date range,
    save to CSV, and return the filtered DataFrame.
    """
    df = pd.read_csv(url, parse_dates=["observation_date"])
    mask = (
        (df["observation_date"] >= start_date)
        & (df["observation_date"] <= end_date)
    )
    df_filtered = df.loc[mask].copy()
    df_filtered.to_csv(output_path, index=False, mode="w")
    return df_filtered

if __name__ == "__main__":
    df_indpro = fetch_indpro_data()
    print(f"✅ Downloaded and saved {len(df_indpro)} rows to {df_indpro!s}")  # or log path

def fetch_publishers(
    csv_path: str = "../data/raw/newspapers/all-the-news-2-1.csv"
) -> pd.DataFrame:
    """
    Return a DataFrame of (publication, n_articles) for every unique publisher.
    """
    query = f"""
        SELECT
          publication,
          COUNT(*) AS n_articles
        FROM read_csv_auto('{csv_path}')
        GROUP BY publication
        ORDER BY n_articles DESC
    """
    df = duckdb.query(query).to_df()
    # drop null/None
    df = df.dropna(subset=["publication"])
    df = df[df.publication != "None"]
    return df


def sample_publisher_articles(
    raw_csv: str = "../data/raw/newspapers/all-the-news-2-1.csv",
    output_dir: str = "../data/processed/newspapers",
    max_samples: int = 10000,
    seed: int = 42
) -> None:
    """
    For each publisher in raw_csv, sample up to max_samples rows and
    write them to output_dir/sample_<publisher_safe>.csv.
    """
    random.seed(seed)
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # fetch list of publishers
    publishers = fetch_publishers(raw_csv)
    for pub in publishers["publication"]:
        safe = re.sub(r'\W+', '_', pub.lower()).strip('_')
        # query all articles for this publisher
        df_pub = duckdb.query(f"""
            SELECT *
              FROM read_csv_auto('{raw_csv}')
             WHERE publication = '{pub.replace("'", "''")}'
        """).to_df()
        # sample & save
        n = min(len(df_pub), max_samples)
        sample_df = df_pub.sample(n=n, random_state=seed)
        out_path = Path(output_dir) / f"sample_{safe}.csv"
        sample_df.to_csv(out_path, index=False)
        print(f"Saved {n} rows for '{pub}' → {out_path}")