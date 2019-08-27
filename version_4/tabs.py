import dash_core_components as dcc
from tab_widgets import tab_widgets_children
from tab_data_table import tab_table_children
from tab_map import tab_map_children
from tab_price_week import tab_price_week_children


tabs = dcc.Tabs(
            id="right-column",
            value='tab_widgets',
            className="eight columns",
            children=[
            dcc.Tab(label='Widgets', value='tab_widgets',
                children=tab_widgets_children),
            dcc.Tab(label='Data Table', value='tab_table',
                children=tab_table_children),
            dcc.Tab(label='Map', value='tab_map',
                children=tab_map_children),
            dcc.Tab(label='Price by Week', value='tab_price_week',
                children=tab_price_week_children),
        ])
