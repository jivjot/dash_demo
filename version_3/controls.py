import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
import data


def get_marks(minvalue,maxvalue,step,step_label):
    ret = {}
    for i in range(0,int(maxvalue+step),step):
        if i >= minvalue and i <= maxvalue:
            if i % step_label == 0:
                ret[i] = {'label':i}
            else:
                ret[i] = {}
    return ret

def get_options(li):
    ret = []
    for l in li:
        ret.append({'label':l,'value':l})
    return ret


invoice_date_range_label = html.P("Invoice Date Range",className="control_label")

invoice_date_range = dcc.DatePickerRange(id='invoice_date_range',
                                    min_date_allowed=data.start_date,
                                    max_date_allowed=data.end_date,initial_visible_month=data.start_date,
                                    start_date = data.start_date,
                                    end_date = data.end_date,
                                    className="dcc_control")

quantity_label = html.P("Quantity",className="control_label")

quantity_slider = dcc.Slider(
                    id='quantity_slider',
                    min=1,
                    max=data.max_qty,
                    value=data.max_qty,
                    tooltip=True,
                    marks = get_marks(1,data.max_qty,4000,8000),
                    className="dcc_control")



unit_price_label = html.P("Unit Price",className="control_label")

unit_price_slider = dcc.RangeSlider(
                        id='unit_price_slider',
                        min=data.min_price,
                        max=data.max_price,
                        tooltip=True,
                        marks = get_marks(data.min_price,
                            data.max_price,50,100),
                        value=[data.min_price, data.max_price],
                        className="dcc_control")

country_label = html.P("Select Country",className="control_label")



country_dropdown =  dcc.Dropdown(
                        options = get_options(data.all_countries),
                        value=['All'],
                        multi=True,
                        id='country_dropdown',
                        className="dcc_control")

text_label = html.P("Text Input",className="control_label")

text_input = dcc.Input(
                id="text_input",
                placeholder="Write your Text Here",
                className="dcc_control"
                )


products_label = html.P("Products",className="control_label")
products_dropdown =  dcc.Dropdown(
                        options = get_options(data.products),
                        value=data.product_default,
                        id='products_dropdown',
                        className="dcc_control")


controls = html.Div([
                        invoice_date_range_label,
                        invoice_date_range,html.Br(),
                        quantity_label,quantity_slider,html.Br(),
                        unit_price_label,unit_price_slider,html.Br(),
                        country_label,country_dropdown,
                        text_label,text_input,
                        html.Br(),html.Br(),html.Br(),
                        products_label,products_dropdown
                    ],
            className="pretty_container four columns",
            id="cross-filter-options"
            )
