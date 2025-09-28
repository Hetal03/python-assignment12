import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# Sample Data
# -----------------------------
np.random.seed(42)  # for reproducibility
sample_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': np.random.randint(100, 500, size=4),
    'Profit': np.random.randint(20, 100, size=4)
}
df = pd.DataFrame(sample_data)

# -----------------------------
# Sidebar: Filter Options
# -----------------------------
st.sidebar.header('Filter Options')
selected_product = st.sidebar.selectbox('Select Product', df['Product'])

# Filter the data based on user selection
filtered_df = df[df['Product'] == selected_product]

# -----------------------------
# Main App
# -----------------------------
st.title('Simple Product Dashboard')

# Display key metrics
col1, col2 = st.columns(2)
with col1:
    st.metric('Sales', f"${filtered_df['Sales'].values[0]:,}")
with col2:
    st.metric('Profit', f"${filtered_df['Profit'].values[0]:,}")

# Bar chart comparing all products
st.subheader('Sales and Profit Comparison')
bar_chart = px.bar(df, x='Product', y=['Sales', 'Profit'], barmode='group')
st.plotly_chart(bar_chart)
