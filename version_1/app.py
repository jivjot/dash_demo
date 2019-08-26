import dash
import dash_html_components as html

app = dash.Dash(__name__,
        meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.layout = html.Div([],
        id="mainContainer",
        style={"display":"flex",
            "flex-direction":"column"}
        )



if __name__ == "__main__":
    app.run_server(debug=False,host='0.0.0.0')
