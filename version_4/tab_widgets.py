import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


invoiceDateRangeInput = dcc.Input(
                            id='invoiceDateRangeInput',
                            placeholder='',
                            disabled=True,
                            value='',
                            style={'width': '100%'},
                            className="dcc_control")

quantityInput = dcc.Input(
                            id='quantityInput',
                            placeholder='',
                            disabled=True,
                            value='',
                            style={'width': '100%'},
                            className="dcc_control")


priceInput = dcc.Input(
                            id='priceInput',
                            placeholder='',
                            disabled=True,
                            value='',
                            style={'width': '100%'},
                            className="dcc_control")

countryInput = dcc.Input(
                            id='countryInput',
                            placeholder='',
                            disabled=True,
                            value='',
                            style={'width': '100%'},
                            className="dcc_control")



textInput = dcc.Input(
                            id='textInput',
                            placeholder='',
                            disabled=True,
                            value='',
                            style={'width': '100%'},
                            className="dcc_control")

tab_widgets_children = [
                        html.Br(),invoiceDateRangeInput,
                        html.Br(),html.Br(),quantityInput,
                        html.Br(),html.Br(),priceInput,
                        html.Br(),html.Br(),countryInput,
                        html.Br(),html.Br(),textInput,
                        ]



