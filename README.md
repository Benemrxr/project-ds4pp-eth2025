# Project DS4PP ETH 2025

*Which features in newspaper articles most accurately forecast U.S. industrial production?* Welcome to the group project repository for the Data Science for Public Policy course at ETH Zurich, 2025.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
    - [Python Environment](#python-environment)
    - [Data Preparation](#data-preparation)

## Project Overview

This project investigates which features derived from newspaper articles in which model specifications best predict U.S. industrial production. We analyze a large corpus of news articles, applying natural language processing techniques to extract relevant features. The project involves:

- Collecting and preprocessing national newspaper data.
- Constructing text-based indicators using methods such as topic modeling and sentiment analysis.
- Building predictive models to forecast U.S. industrial production, comparing models using all national news with those that are filtered on economic articles.
- Evaluating model performance and interpreting the impact of different features.

For a detailed project outline, see our project report.

## Getting Started

Follow these instructions to set up your development environment.

### Python Environment

This project requires **Python 3.12**.

#### Setting up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment named '.venv'
python3.12 -m venv .venv
# or
py -3.12 -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

#### Installation

After activating your virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Data preparation

Two data preparation steps:

1. Download main newspaper file
2. Run dataprep source code

#### 1. Main Newspaper File

The newspaper dataset for this project is called **All The News 2.0** created by Andrew Thompson and made available by [components.one](https://components.one/datasets/all-the-news-2-news-articles-dataset). The dataset is hosted on ProtonDrive, which does not allow for an automatic download.

Therefore, please download the dataset manually yourself following the download box at the end of this page: [components.one](https://components.one/datasets/all-the-news-2-news-articles-dataset).

The file is 3.1 GB compressed, 8.8 GB uncompressed. 

Unzip the dataset in this folder: `data/raw/newspaper`.

#### 2. Run dataprep source code

From the project root, run the following code to run the data preparation script:

```bash
python src/dataset.py
```

Observe the terminal output to see if the data preparation process is completed.

## Repository Overview

This repository contains all the source code ([src](https://github.com/Benemrxr/project-ds4pp-eth2025/tree/main/src)), some data files for faster replication ([data](https://github.com/Benemrxr/project-ds4pp-eth2025/tree/main/data)), as well as some stored results ([models](https://github.com/Benemrxr/project-ds4pp-eth2025/tree/main/models) and [plots](https://github.com/Benemrxr/project-ds4pp-eth2025/tree/main/plots)).

Finally, our analysis is described step-by-step in the various ([notebooks](https://github.com/Benemrxr/project-ds4pp-eth2025/tree/main/notebooks)). Note the labels and ordering.

## Contact

- For any questions or feedback feel free to reach our to any of us [contributors](https://github.com/Benemrxr/project-ds4pp-eth2025/graphs/contributors)!