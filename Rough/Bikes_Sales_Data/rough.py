"""
Overview
1. Project Title

"""
import streamlit as st
import pandas as pd


# Project Title
st.title("Analysis of Bike Sales 🏍")

with st.sidebar:
    st.title(":blue[Bike Sales Analysis]")
    st.button("Description")
    st.button("Objective")
    st.button("Dataset Load")
    st.button("Dataset Explain")

#  (a) Description
st.header(":blue[🔷 Description]")
"""
This dataset is about Bike sales in which uncleaned data is available which leads to low accuracy and poor performance of the model.
So, before performing any kind of analysis the data set should be cleaned.
"""

#  (b) Objective
st.header(":blue[🔷 Objective]")
st.write("The main objective of Bike Sales Data is to analysis the data for visualization.")

#  (c) Dataset Load
df = pd.read_excel("bike_sales.xlsx")
st.header(":blue[🔷 Dataset Load]")
if st.checkbox("Show Bike Sales dataset"):
    st.dataframe(df)

# (d) Dataset Explanation
st.header(":blue[🔷 Dataset Explanation:-]")
# 1. Columns
if st.checkbox("🔹 Total number of Columns:-"):
    st.write("19")

# 2.Rows
if st.checkbox("🔹 Total number of Rows:- "):
    st.write("139")
# 3.Missing Values
# Information of dataframe


left_column, right_column = st.columns(2)
with left_column:
    st.subheader("🔹 Data of Missing values-")
    missing_data = df.isnull().sum()
    st.dataframe(missing_data)
with right_column:
    st.subheader("🔹 Full Statistics of Dataset")
    dataset_info = df.describe()
    dataset_info = df.describe()
    st.write(dataset_info)

# 4.Duplicate Values
st.subheader("🔹 Total number of Duplicate values:-")
# 5. Types of Columns
st.subheader("🔹 Types of Column:-")