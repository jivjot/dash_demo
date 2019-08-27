from dash.dependencies import Input, Output
from dateutil import parser


def set_invoice_date_range(start_date,end_date):
    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)
    return "InvoiceDate Range is {} to {}".format(start_date.date(),
            end_date.date())



def set_callbacks(app):
    input_array = [Input("invoice_date_range", "start_date"),
                Input("invoice_date_range", "end_date")]
    @app.callback(Output("invoiceDateRangeInput", "value"),input_array)
    def func(start_date,end_date):
        return set_invoice_date_range(start_date,end_date)


    input_array = [Input("quantity_slider", "value")]
    @app.callback(Output("quantityInput", "value"),input_array)
    def func(value):
        return "Quantity Slider Value is {}".format(value)


    input_array = [Input("unit_price_slider", "value")]
    @app.callback(Output("priceInput", "value"),input_array)
    def func(value):
        return "Price Slider Range is {} to {}".format(value[0],value[1])


    input_array = [Input("country_dropdown", "value")]
    @app.callback(Output("countryInput", "value"),input_array)
    def func(value):
        return "Countries selected are {}".format(', '.join(value))



    input_array = [Input("text_input", "value")]
    @app.callback(Output("textInput", "value"),input_array)
    def func(value):
        if value is None:
            return ''
        return "Text: {}".format(value)
