import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/ismarfrango/visualizacaoCS/master/southAmerica-pop.csv')

fig = go.Figure(data=go.Choropleth(
    locations = df['name'],
    z = df['pop'].astype(int),
    locationmode = 'country names',
    colorscale = 'Reds',
    colorbar_title = 'População',
))

fig.update_layout(
    title_text = 'População da América do Sul - 2019',
    geo_scope = 'south america',
)

fig.show()