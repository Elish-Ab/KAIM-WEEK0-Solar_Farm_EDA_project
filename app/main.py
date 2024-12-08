import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

# App title
st.title("Solar Data Analysis Dashboard")

# Load dataset selection from the sidebar
dataset_choice = st.sidebar.selectbox("Select Dataset", ['benin', 'sierraleone', 'togo'])

# Load data based on user selection
if dataset_choice == 'benin':
    data = pd.read_csv('benin-malanville.csv')
elif dataset_choice == 'sierraleone':
    data = pd.read_csv('sierraleone-bumbuna.csv')
else:
    data = pd.read_csv('togo-dapaong_qc.csv')

# Data preview
st.subheader(f"Displaying {dataset_choice} Data")
st.write(data.head())

# Anomaly detection
if st.sidebar.checkbox("Detect Anomalies Using Z-Score"):
    anomalies = detect_anomalies(data)
    st.write(f"Found {len(anomalies)} anomalies")
    st.write(anomalies)

# Cleaned data preview
if st.sidebar.checkbox("Clean Data"):
    cleaned_data = clean_data(data)
    st.write(f"Cleaned Data (Rows: {len(cleaned_data)})")
    st.write(cleaned_data)

# Show time series plot
if st.sidebar.checkbox("Show Time Series Plot"):
    time_column = st.sidebar.selectbox("Select time column", data.columns)
    if time_column:
        data[time_column] = pd.to_datetime(data[time_column])
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(data[time_column], data['GHI'], label='GHI', color='blue')
        ax.set_title(f"Time Series of {dataset_choice} GHI")
        ax.set_xlabel("Date")
        ax.set_ylabel("GHI")
        ax.legend()
        st.pyplot(fig)

# Correlation heatmap
if st.sidebar.checkbox("Show Correlation Heatmap"):
    correlation_matrix = data[['GHI', 'DNI', 'DHI', 'Tamb', 'WS', 'WSgust']].corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Z-score plot for GHI
if st.sidebar.checkbox("Show Z-Score Plot for GHI"):
    z_scores = data['GHI'].apply(zscore)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(data.index, z_scores, label='GHI Z-Score')
    ax.axhline(3, color='red', linestyle='--', label='Outlier Threshold (+3)')
    ax.axhline(-3, color='red', linestyle='--', label='Outlier Threshold (-3)')
    ax.set_title("Z-Score Plot for GHI")
    ax.set_xlabel("Index")
    ax.set_ylabel("Z-Score")
    ax.legend()
    st.pyplot(fig)
