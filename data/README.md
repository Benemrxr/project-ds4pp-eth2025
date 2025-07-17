# 📁 data/

This folder contains all datasets used and generated during the project. It is organized to separate raw inputs from processed outputs.


## File Descriptions

| File/Folder                             | Description |
|----------------------------------------|-------------|
| `raw/`                           | Contains all raw data sets. The Loughran-McDonald financial sentiment dictionary, the industrial production index, and the primary news corpus. |
| `raw/newspapers/`                           | Contains the "All the News 2.1" data set. ⚠️ Not committed to version control due to size. |
| `raw/INDPRO.csv`                            | Monthly U.S. Industrial Production Index (target variable). ⚠️ Not committed to version control, automated download. |
| `raw/Loughran_McDonald_MasterDictionary_1993-2024.csv`                           | Contains the Loughran-McDonald financial sentiment dictionary. |
| `processed/`                           | Contains nall processed data sets. |
| `processed/newspapers/`                           | Contains all newspaper articles sampled by the different publishers.  |
| `processed/monthly_sentiment_all.csv`            | Output of sentiment analysis by publisher and month. |
| `processed/monthly_topic_shares_by_publisher.csv`| Aggregated topic distributions from LDA model by month and publisher. |

## ⚠️ Notes

- The sentiment and topic share files are generated artifacts — should be reproducible from the notebooks.
