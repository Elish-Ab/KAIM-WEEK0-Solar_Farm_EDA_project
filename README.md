# KAIM WEEK0 Project

## Overview

This project involves analyzing solar radiation and weather data from three different countries (Benin, Sierra Leone, and Togo). The data analysis includes data cleaning, exploratory data analysis (EDA), and visualization. Additionally, an interactive dashboard is created using **Streamlit** to visualize the insights and interact with the data dynamically. Finally, the dashboard is deployed on **Streamlit Community Cloud** for public access.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Data Analysis](#data-analysis)
  - [Data Quality Check](#data-quality-check)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Time Series Analysis](#time-series-analysis)
  - [Correlation Analysis](#correlation-analysis)
  - [Outlier Detection and Z-Score Analysis](#outlier-detection-and-z-score-analysis)
  - [Wind & Temperature Analysis](#wind--temperature-analysis)
- [Dashboard Development](#dashboard-development)
- [Deployment](#deployment)
- [Usage

## Project Structure

├── .streamlit │ └── config.toml 
├── .vscode │ └── settings.json 
├── .github │ └── workflows │ ├── unittests.yml 
├── .gitignore 
├── requirements.txt 
├── README.md 
├── notebooks │ ├── init.py │ ├── EDA.ipynb │ └── README.md 
├── tests │ ├── init.py 
├── app │ ├── init.py │ ├── main.py # main Streamlit application script │ ├── utils.py # utility functions for data processing and visualization └── scripts ├── init.py └── README.md


---

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
       git clone https://github.com/yourusername/KAIM-WEEK0.git
       cd KAIM-WEEK0
2. **Create a virtual environment (optional but recommended):**
  ```bash
       python -m venv .venv
       source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```
3. Install the required dependencies:
  ```bash
      pip install -r requirements.txt
  ```
## Data Analysis
 Data Quality Check

    Missing Values: Identified missing values in the datasets (Benin, Sierra Leone, and Togo) and applied imputation or removal strategies.

    Outliers Detection: Applied Z-score analysis to detect anomalies in columns such as GHI, DNI, DHI, Tamb, WS, WSgust.

    Incorrect Entries: Filtered out incorrect entries, e.g., negative values for columns that should only contain positive values.

## Exploratory Data Analysis (EDA)

EDA was performed on the solar radiation and weather data to understand the distribution, identify trends, and visualize correlations.

    Boxplots: Visualized the distribution of key variables (GHI, DNI, DHI, WS, Tamb) to check for outliers and patterns.
    Histograms: Used histograms to check the frequency distribution of variables like GHI, DNI, and Tamb.
    Pairplots: Visualized pairwise relationships between key variables to identify correlations.

Time Series Analysis

    Line Charts: Plotted time series data of GHI, DNI, DHI, and Tamb over time to identify daily, monthly, and seasonal trends.
    Anomalies: Identified peaks or sudden changes in the data that may indicate anomalies (e.g., spikes in solar radiation).

Correlation Analysis

    Correlation Matrix: Used a heatmap to visualize correlations between variables like GHI, DNI, DHI, Tamb, and WSgust.
    Scatter Plots: Investigated the relationship between wind conditions (WS, WSgust) and solar irradiance using scatter plots.

Outlier Detection and Z-Score Analysis

Performed Z-score analysis to detect outliers in the following columns: GHI, DNI, DHI, Tamb, WS, WSgust.
