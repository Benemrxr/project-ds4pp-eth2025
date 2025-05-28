# Project DS4PP ETH 2025

*Which features in newspaper articles most accurately forecast U.S. industrial production?* Welcome to the group project repository for the Data Science for Public Policy course at ETH Zurich, 2025.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Python Environment](#python-environment)
- [Installation](#installation)

## Project Overview

This project investigates which features derived from newspaper articles in which model specifications best predict U.S. industrial production. We analyze a large corpus of news articles, applying natural language processing techniques to extract relevant features. The project involves:

- Collecting and preprocessing national newspaper data.
- Constructing text-based indicators using methods such as topic modeling and sentiment analysis.
- Building predictive models to forecast U.S. industrial production, comparing models using all national news with those that are filtered on economic articles.
- Evaluating model performance and interpreting the impact of different features.

For a detailed project outline, see our [Overleaf project](https://www.overleaf.com/project/67fd24e6b55bac29453657d7).

## Getting Started

Follow these instructions to set up your development environment.

### Python Environment

This project requires **Python 3.12**.

### Setting up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment named '.venv'
python3.12 -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Installation

After activating your virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Data preparation

Manually source the "All the News 2.1" data set from ProtonDrive. No automated download possible. See instructions in the data folder.