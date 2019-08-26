import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__,
        meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)


plotly_image = html.Img(src=app.get_asset_url("dash-logo.png"),
                    id="plotly-image",
                    style={"height":"60px","width":"auto","margin-bottom":"25px"},
                    className="one-third column"
                    )

header_middle = html.Div(
                    [
                        html.H3("",style={"margin-bottom": "0px"},),
                        ],
                    id="title",
                    className="one-half column"
                    )

header_right = html.A(
                html.Button("Learn More", id="learn-more-button"),
                href="https://plot.ly/dash/pricing/",
                className="one-third column",
                id="button"
                )


header = html.Div(
        [plotly_image,header_middle,header_right],
        className="row flex-display",
        id="header",
        style={"margin-bottom":"25px"}
        )

layout_children = [header]

app.layout = html.Div(layout_children,
        id="mainContainer",
        style={"display":"flex",
            "flex-direction":"column"}
        )



if __name__ == "__main__":
    app.run_server(debug=False,host='0.0.0.0')
