import plotly as py
import plotly.graph_objects as go


data = dict(
    type = 'choropleth',
    locations = ['USA', 'Spain', 'Italy', 'UK', 'France', 'Germany', 'Russia', 'Turkey', 'Brazil', 'Iran'],
    locationmode='country names',
    colorscale = ['yellow', 'orange', 'red'],
    z = [1188122,247122,210717,186599,168693,165664,134687,126045,101147,97424])
map = go.Figure(data=[data])
map.show()