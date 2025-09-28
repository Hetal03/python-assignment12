# wind_plotly.py
# Assignment 12 - Task 3: Interactive Visualizations with Plotly
# Load the Plotly wind dataset and create an interactive scatter plot

import plotly.express as px
import plotly.data as pldata
import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# -----------------------------
# Data Cleaning
# -----------------------------
# Convert 'strength' column to float
df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)

# -----------------------------
# Create Interactive Scatter Plot
# -----------------------------
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency',
    hover_data=['direction', 'strength', 'frequency']
)

# -----------------------------
# Save to HTML and Open
# -----------------------------
fig.write_html("wind.html", auto_open=True)

print("Interactive plot saved as 'wind.html'. Open this file in a browser to view the visualization.")
