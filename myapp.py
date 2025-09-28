# myapp.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
df = px.data.gapminder()

# Get unique countries for dropdown
countries = df['country'].unique()

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "GDP Per Capita Dashboard"

# App layout
app.layout = html.Div([
    html.H1("GDP Per Capita Dashboard", style={'textAlign': 'center'}),
    
    html.Label("Select a Country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'  # default selection
    ),
    
    dcc.Graph(id='gdp-growth')
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    # Filter dataset for the selected country
    filtered_df = df[df['country'] == selected_country]
    
    # Create line plot for GDP per capita
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f'GDP per Capita Growth for {selected_country}',
        markers=True
    )
    
    fig.update_layout(yaxis_title='GDP per Capita', xaxis_title='Year')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
