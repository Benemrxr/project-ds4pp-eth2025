# Project DS4PP ETH 2025

*Do regional newspaper articles improve the predictive power of national news in forecasting U.S. industrial production?* Welcome to the group project repository for the Data Science for Public Policy course at ETH Zurich, 2025.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Python Environment](#python-environment)
- [Installation](#installation)

## Project Overview

This project investigates whether incorporating regional newspaper articles enhances the ability of national news to forecast U.S. industrial production. We analyze a large corpus of news articles, applying natural language processing techniques to extract relevant features. The project involves:

- Collecting and preprocessing national and regional newspaper data.
- Constructing text-based indicators using methods such as topic modeling and sentiment analysis.
- Building predictive models to forecast U.S. industrial production, comparing models using only national news with those that also include regional news.
- Evaluating model performance and interpreting the impact of regional news coverage.

For a detailed project outline, see our [Overleaf project](https://www.overleaf.com/project/67fd24e6b55bac29453657d7).

## Getting Started

Follow these instructions to set up your development environment.

## Python Environment

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

## Installation

After activating your virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```
