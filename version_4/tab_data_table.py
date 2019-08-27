import dash_table
import data


table = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in data.data.columns],
        data = data.data.head().to_dict('records'),
        page_size=10,
        sort_action='native',
        filter_action='native'
        )

tab_table_children = [table]
