# 📓 Notebooks

## Notebook Structure

| Notebook | Purpose |
|----------|---------|
| `01_exploration.ipynb`         | Initial data inspection, data source overview, and basic cleaning steps. |
| `02_topic_modeling.ipynb`      | LDA topic modeling using Gensim; includes preprocessing and model saving. |
| `03_sentiment_analysis.ipynb`  | Sentiment score computation using dictionary-based or NLP methods. |
| `04_feature_engineering.ipynb` | Merging topic shares, sentiment, and external data (e.g., IPI). |
| `05_model_training.ipynb`      | Model comparison (XGBoost, RandomForest, Ridge, etc.) with RMSE evaluation. |
| `06_shap_explainer.ipynb`      | SHAP values and feature importance interpretation for top model(s). |

## Guidelines

- Run the notebooks in order unless noted otherwise.

## Old notebooks

| Notebook | Purpose |
|----------|---------|
| `GDELT-IPI.ipynb`         | Notebook to get GDELT events **(to be deleted?)** |
| `industrial-production.ipynb`      | Downloads and saves the INDPRO variable from FRED. **(to be moved into a script)** |
| `national_news.ipynb`  | Load and sample articles. Sentiment score computation using dictionary-based method. Topic modeling on all samples. Model training and evalutation. **(to be restructured into different files)** |
| `Supervised.ipynb` | Filtered articles by economic keywords. TF-IDF feature extraction, model training and evaluation. **(to be restructured, and add topic shares)** |
