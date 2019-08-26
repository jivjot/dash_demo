import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
import data


invoice_date_range_label = html.P("Invoice Date Range",
                            className="control_label"
                            )

invoice_date_range = dcc.DatePickerRange(
                        id='invoice_date_range',
                        min_date_allowed=data.start_date,
                        max_date_allowed=data.end_date,
                        initial_visible_month=data.start_date,
                        start_date = data.start_date,
                        end_date = data.end_date,
                        className="dcc_control"
                        )

controls = html.Div([
                        invoice_date_range_label,
                        invoice_date_range,
                    ],
            className="pretty_container four columns",
            id="cross-filter-options"
            )
