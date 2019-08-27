import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as d
import plotly.express as px
import data
import dash_table


data = data.data[data.data.StockCode == data.product_default]
agg_data = data[['StockCode','Description','Weeknumber','WeeklyPrice','stdWeeklyPrice']].drop_duplicates()


styles = {
        'pre': {
            'border': 'thin lightgrey solid',
            'overflowX': 'scroll'
            }
        }

fig = px.scatter(agg_data, x="Weeknumber", y="WeeklyPrice",color='StockCode',
                         error_y="stdWeeklyPrice",
                         error_y_minus="stdWeeklyPrice")


graph = dcc.Graph(
            id='basic-interactions',
            figure=fig
            )


table = dash_table.DataTable(
        id='table_price_week',
        columns=[{"name": i, "id": i} for i in data.columns],
        data=data.to_dict('records'),
        page_size=10,
        sort_action='native',
        filter_action='native'
        )


click_data = html.Div(className='row', children=[
	    html.Div([
		dcc.Markdown(d("""
		    **Hover Data**

		    Mouse over values in the graph.
		""")),
		html.Pre(id='hover-data', style=styles['pre'])
	    ], className='three columns'),

	    html.Div([
		dcc.Markdown(d("""
		    **Click Data**

		    Click on points in the graph.
		""")),
		html.Pre(id='click-data', style=styles['pre']),
	    ], className='three columns'),

	    html.Div([
		dcc.Markdown(d("""
		    **Selection Data**

		    Choose the lasso or rectangle tool in the graph's menu
		    bar and then select points in the graph.

		    Note that if `layout.clickmode = 'event+select'`, selection data also
		    accumulates (or un-accumulates) selected data if you hold down the shift
		    button while clicking.
		""")),
		html.Pre(id='selected-data', style=styles['pre']),
	    ], className='three columns'),

	    html.Div([
		dcc.Markdown(d("""
		    **Zoom and Relayout Data**

		    Click and drag on the graph to zoom or click on the zoom
		    buttons in the graph's menu bar.
		    Clicking on legend items will also fire
		    this event.
		""")),
		html.Pre(id='relayout-data', style=styles['pre']),
	    ], className='three columns')
	])



tab_price_week_children = [graph,table,click_data]
