from dash import Dash , dcc, callback, Input, Output, html
import pandas as pd 
import plotly.express as px


# DATA 
spotify_df = pd.read_csv("data/spotify_data_clean.csv")

spotify_df.fillna('UNKNOWN', inplace=True)


# make release date numeric 
spotify_df['album_release_date'] = pd.to_datetime(spotify_df['album_release_date'])

# make a year column 
spotify_df['Year'] = spotify_df['album_release_date'].dt.year

app = Dash(__name__, title="Spotify App")


# Components
graph1 = dcc.Graph(id="pie-chart-1")

dd1  = dcc.Dropdown(spotify_df.Year.unique(), 
                    placeholder="Select a year...", 
                    id="dd-year")

app.layout = [
        html.H1(children = "Spotify Data", style={'textAlign': 'center'}),
        dd1,
        graph1 
]

@callback(
    Output('pie-chart-1', 'figure'),
    Input('dd-year', 'value')

)
def update_pie(value):

    cond1 = value == spotify_df.Year
    cond2 = "UNKNOWN" != spotify_df.artist_genres
    

    top_genre_types_df = spotify_df[cond1 & cond2]['artist_genres'].value_counts()[:20]



    fig = px.pie(top_genre_types_df, 
                 values="count", 
                 names=top_genre_types_df.index, 
                 title='Most Populare Genre by Year'
                 )
    
    fig.update_layout(height=700)


    return fig

if __name__ == '__main__':
    app.run(debug=True)