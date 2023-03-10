from utils import load_data
from datetime import date
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# Create a dash application
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

# Load data
df = load_data(r"data/VAERS", "vaccine")

# Calculate the max_time and min_time for date picker
max_time = df['RECVDATE'].max()
min_time = df['RECVDATE'].min()

# Calculate the max_age and min_age for age slider
max_age = df['AGE_YRS'].max()
min_age = df['AGE_YRS'].min()

# Create an app layout
app.layout = html.Div(children=[
    # Add title to the dashboard
    html.H1('Vaccine Death Records Dashboard',
            style={'textAlign': 'center', 'color': '#FF0000', 'font-size': 40}),

    # Create an outer division
    html.Div([
        # Add the division for choosing age
        html.Div([
            html.H2("Age:"),
            dcc.RangeSlider(
                id='age-slider',
                min=0,
                max=120,
                step=10,
                value=[min_age, max_age]
            ),
        ]),

        # Add the next division for choosing time
        html.Div([
            html.H2("Time Range:"),
            dcc.DatePickerRange(
                id='date-picker-range',
                min_date_allowed=min_time,
                max_date_allowed=max_time,
                initial_visible_month=date(2010, 6, 27),
                end_date=max_time
            ),
        ]),
    ]),

    # Add computed graph
    html.Br(),
    html.Div([
        html.Div([], id='plot-1'),
        html.Div([], id='plot-2')
    ], style={'display': 'flex'}),
])


# Add a callback function for `gender, age-group, received-year` as input, `record-chart` as output
@app.callback([Output(component_id='plot-1', component_property='children'),
               Output(component_id='plot-2', component_property='children')],

              [Input(component_id='age-slider', component_property='value'),
               Input(component_id='date-picker-range', component_property='start_date'),
               Input(component_id='date-picker-range', component_property='end_date')]
              )
def get_graph(age, start_date, end_date):
    # Compute required information for creating graph from the data
    filtered_df = df.drop(df[df['VAX_TYPE'] == 'COVID19'].index, axis=0)
    filtered_df = filtered_df[filtered_df['DIED'] == 'Y']
    filtered_df = filtered_df[filtered_df['AGE_YRS'].between(age[0], age[1])]
    filtered_df = filtered_df.loc[(filtered_df['RECVDATE'] > start_date) & (filtered_df['RECVDATE'] <= end_date)]

    # Group the data by vaccine type and sex. Compute total number of deaths in each combination
    bar_data = filtered_df.groupby(['VAX_TYPE', 'SEX'])['DIED'].count().reset_index()

    bar_fig = px.bar(bar_data, x="VAX_TYPE", y="DIED", color="SEX",
                     title='Total number of deaths by vaccine types')

    bar_fig.update_xaxes(tickangle=60)

    # Group the data by state, then compute the number of deaths in each state using choropleth
    map_data = filtered_df.groupby(['STATE'])['DIED'].count().reset_index()

    map_fig = px.choropleth(map_data,
                            locations='STATE',
                            color='DIED',
                            hover_data=['STATE', 'DIED'],
                            locationmode='USA-states',
                            color_continuous_scale='GnBu',
                            range_color=[0, map_data['DIED'].max()])

    map_fig.update_layout(
        title_text='Number of deaths from different states',
        geo_scope='usa')

    return [dcc.Graph(figure=bar_fig),
            dcc.Graph(figure=map_fig)]


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
