Make sure to manually download the `All-the-News 2.0` (2.1) dataset from [components.one / protondrive](https://components.one/datasets/all-the-news-2-news-articles-dataset) beforehand!

# Source Code

This folder contains all python soure code files:
| Source code | Purpose |
|----------|---------|
| `dataset.py`         | Preparation of data sets used in the notebooks: 1) fetch INDPRO data, 2) fetch publishers, 3) sample articles by publishers, 4) append INDPRO to each publisher for sLDA model. |

 Before running the data preparation functions, the script makes sure that the large newspaper data set is installed and unzipped in the appropriate folder, else it prompts the user to do so. Note that you have to run the script from the project root with: 
```bash
python src/dataset.py
```