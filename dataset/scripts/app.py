import streamlit as st
import pandas as pd

st.title("📊 TrendVision Analytics Dashboard")

df = pd.read_csv("dataset/trends_data.csv")

df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

platform = st.selectbox(
    "Choose a platform",
    df["Platform"].unique()
)

filtered = df[df["Platform"] == platform]

st.dataframe(filtered)

st.bar_chart(filtered["Engagement"])
