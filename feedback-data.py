# Import required libraries
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Load the CSV data directly from the GitHub URL into a Pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/icoldigital/mygit-datasets/main/dictionary_data_2023-10-24_16-49-17.csv')

# Create a simple bar chart using Plotly Express
# Replace 'labels' and 'source' with the actual columns you want to visualize
fig = px.bar(df, x='labels', y='source')

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Customer Feedback Dashboard"),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
