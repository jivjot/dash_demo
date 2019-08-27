from dash.dependencies import Input, Output
import data

def set_callbacks(app):
    input_array = [Input("invoice_date_range", "start_date"),
                Input("invoice_date_range", "end_date"),
                Input("quantity_slider","value"),
                Input("unit_price_slider","value"),
                Input("country_dropdown","value")]

    @app.callback(Output("table", "data"),input_array)
    def func(start_date,end_date,quantity,price_range,country):
        local_data = data.data
        local_data= local_data[local_data.InvoiceDate >= start_date]
        local_data = local_data[local_data.InvoiceDate <= end_date]
        local_data= local_data[local_data.Quantity <= quantity]
        local_data= local_data[local_data.UnitPrice >= price_range[0]]
        local_data = local_data[local_data.UnitPrice <= price_range[1]]
        if country == [] or country == ['All']:
            return local_data.to_dict('records')
        else:
            print (country)
            local_data = local_data[local_data.Country.isin(country)]
            return local_data.to_dict('records')




