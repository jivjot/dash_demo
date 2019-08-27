import dash_core_components as dcc
import plotly.graph_objects as go
import data

mapbox_access_token = open(".mapbox_token").read()



fig = go.Figure(go.Scattermapbox(
        lat=data.cities.Latitude.values,
        lon=data.cities.Longitude.values,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=data.cities.City.values
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=data.cities.Latitude.mean(),
            lon=data.cities.Longitude.mean()
        ),
        pitch=0,
        zoom=5,
    ),
)

map_ = dcc.Graph(
        id='basic-interactions',
        figure=fig,
        style={'height': 900}
        )


tab_map_children = [map_]
