from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load Gapminder dataset
df = px.data.gapminder()

# Create a list of unique countries for the dropdown
countries = df['country'].unique()

# Initialize Dash app
app = Dash(__name__)
server = app.server

# Layout: HTML + Dash components
app.layout = html.Div([
    html.H1("GDP per Capita Over Time", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada",  # Default selected country
        style={'width': '50%', 'margin': 'auto'}
    ),
    
    dcc.Graph(id="gdp-growth")
])

# Callback: updates graph based on dropdown selection
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    # Filter dataset for selected country
    filtered_df = df[df['country'] == selected_country]
    
    # Create line plot for GDP per capita
    fig = px.line(
        filtered_df, 
        x="year", 
        y="gdpPercap", 
        title=f"GDP per Capita for {selected_country}", 
        markers=True
    )
    fig.update_layout(yaxis_title="GDP per Capita ($)", xaxis_title="Year")
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
