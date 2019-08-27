import dash_core_components as dcc

tabs = dcc.Tabs(id="right-column", value='tab_widgets',
            className="pretty_container eight columns",
            children=[
            dcc.Tab(label='Widgets', value='tab_widgets'),
            dcc.Tab(label='Data Table', value='tab_table'),
            dcc.Tab(label='Map', value='tab_map'),
            dcc.Tab(label='Price by Week', value='tab_price_week'),
        ])
