from dash import Dash , dcc, callback, Input, Output
import pandas as pd 
import plotly.express as px


# DATA 
spotify_df = pd.read_csv("data/spotify_data_clean.csv")

app = Dash(__name__, title="Spotify App")

app.layout = [
    
]

if __name__ == '__main__':
    app.run(debug=True)