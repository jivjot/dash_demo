from dash.dependencies import Input, Output
import json
import plotly.express as px
import data

def get_figure(value):
    agg_data = data.data[data.data.StockCode == value]
    columns = ['StockCode','Description','Weeknumber','WeeklyPrice','stdWeeklyPrice']
    agg_data = agg_data[columns].drop_duplicates()
    fig = px.scatter(agg_data, x="Weeknumber", y="WeeklyPrice",color='StockCode',
                             error_y="stdWeeklyPrice",
                             error_y_minus="stdWeeklyPrice")
    return fig




def set_callbacks(app):

    input_array = [Input("products_dropdown", "value")]
    @app.callback(Output("basic-interactions", "figure"),input_array)
    def func(value):
        return get_figure(value)

    input_array = [Input("basic-interactions", "clickData"),
            Input("products_dropdown","value")]
    @app.callback(
        Output('table_price_week', 'data'),input_array)
    def func(clickData,product):
        agg_data = data.data[data.data.StockCode == product]
        if clickData is not None:
            week = clickData['points'][0]["x"]
            agg_data = agg_data[agg_data.Weeknumber == week]
        return agg_data.to_dict('records')


    @app.callback(
            Output('hover-data', 'children'),
            [Input('basic-interactions', 'hoverData')])
    def display_hover_data(hoverData):
        return json.dumps(hoverData, indent=2)


    @app.callback(
        Output('click-data', 'children'),
        [Input('basic-interactions', 'clickData')])
    def display_click_data(clickData):
        return json.dumps(clickData, indent=2)


    @app.callback(
        Output('selected-data', 'children'),
        [Input('basic-interactions', 'selectedData')])
    def display_selected_data(selectedData):
        return json.dumps(selectedData, indent=2)


    @app.callback(
        Output('relayout-data', 'children'),
        [Input('basic-interactions', 'relayoutData')])
    def display_selected_data(relayoutData):
        return json.dumps(relayoutData, indent=2)

