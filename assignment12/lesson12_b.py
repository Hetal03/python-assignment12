import plotly.express as px
import plotly.data as pldata

# Load the Iris dataset
df = pldata.iris(return_type='pandas')  # Returns a Pandas DataFrame

# Create interactive scatter plot
fig = px.scatter(
    df,
    x='sepal_length',
    y='petal_length',
    color='species',
    title="Iris Data: Sepal vs Petal Length",
    hover_data=["petal_length"]
)

# Save as HTML and open in browser
fig.write_html("iris.html", auto_open=True)
