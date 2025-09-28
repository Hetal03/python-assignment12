import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# Section 1: Basic Text & Data
# -----------------------------
st.title("My First Streamlit App")
st.header("Section 1")
st.subheader("Header")
st.subheader("Subheader")
st.text("Simple text")
st.markdown("**Bold** and *italic* text")
st.write("Automatic data display")
st.code("print('Hello World')", language='python')
st.latex(r"\int_{a}^{b} x^2 dx")

# -----------------------------
# Section 2: Input Components
# -----------------------------
st.header("Section 2")

# Text input
name = st.text_input("Enter your name", "John Doe")
description = st.text_area("Description", "Write something...")

# Numeric input
age = st.number_input("Age", min_value=0, max_value=120, value=25)
score = st.slider("Score", 0, 100, 50)

# Selection widgets
option = st.selectbox("Choose an option", ["A", "B", "C"])
options = st.multiselect("Multiple options", ["X", "Y", "Z"])

# Date and time
date = st.date_input("Select date")
time = st.time_input("Select time")

# Buttons and checkbox
if st.button("Click me"):
    st.write("Button clicked!")
    
if st.checkbox("Show/Hide"):
    st.write("Visible content")

# -----------------------------
# Section 3: Layout & Containers
# -----------------------------
st.header("Section 3")

# Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

# Expanders
with st.expander("Click to expand"):
    st.write("Expanded content here")

# Sidebar
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])

# Extra content in col1
with col1:
    st.write("Additional content inside column 1")

# -----------------------------
# Section 4: Simple Dashboard with Sample Data
# -----------------------------
st.header("Section 4: Sample Product Dashboard")

# Sample data
np.random.seed(42)
sample_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': np.random.randint(100, 500, size=4),
    'Profit': np.random.randint(20, 100, size=4)
}
df = pd.DataFrame(sample_data)

# Sidebar filter
st.sidebar.header('Filter Options')
selected_product = st.sidebar.selectbox('Select Product', df['Product'])
filtered_df = df[df['Product'] == selected_product]

# Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric('Sales', f"${filtered_df['Sales'].values[0]:,}")
with col2:
    st.metric('Profit', f"${filtered_df['Profit'].values[0]:,}")

# Bar chart comparing all products
st.subheader('Sales and Profit Comparison')
bar_chart = px.bar(df, x='Product', y=['Sales', 'Profit'], barmode='group')
st.plotly_chart(bar_chart)
