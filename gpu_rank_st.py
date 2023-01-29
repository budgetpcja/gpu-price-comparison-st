import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("gpu_price_performance_ranking_automated.csv")
df["Median Price"] = df["Median Price"].apply(lambda x: float(x.replace("$", "").replace(",", "")))
df["Performance"] = df["Performance"].apply(lambda x: float(x.replace("%", "")))

# create a scatter plot with plotly
fig = px.scatter(
    df,
    x = "Median Price",
    y = "Performance",
    hover_data = ["Graphics Card"],
    labels = {
        "Median Price": "Median Price (USD)",
        "Performance": "Performance (%)",
        "Graphics Card": "Graphics Card"
    }
)
st.set_page_config(layout="wide")
st.title("BPC JA's GPU Price to Performance Ranking Jan 2023")
st.plotly_chart(fig, use_container_width=True)

