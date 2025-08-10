from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np


app = Dash()

# Read file csv
file = 'D:\Technical Test\LuxuryLoanPortfolio.csv'
df = pd.read_csv(file)

# Summary 1
df['funded_amount_mio'] = df['funded_amount'] / 1_000_000
df_funded_purpose = df.groupby('purpose', as_index=False)['funded_amount_mio'].sum()

fig_1 = px.bar(
    df_funded_purpose, 
    x='purpose', 
    y='funded_amount_mio',
    text='funded_amount_mio',
    title='Funded Amount by Loan Purpose',
    labels={'funded_amount_mio':'Funded Amount (in Mio)','purpose':'Loan Purpose'}
)

fig_1.update_traces(texttemplate='%{text:.2f}', textposition='outside')


# Summary 2
df['funded_date'] = pd.to_datetime(df['funded_date'])
df['funded_month'] = df['funded_date'].dt.to_period('M').astype(str)
df['funded_year'] = df['funded_date'].dt.year
df_funded_monthly = df.groupby('funded_month', as_index=False)['loan_id'].count()

fig_2 = px.line(
    df_funded_monthly,
    x='funded_month',
    y='loan_id',
    text='loan_id',
    title='Monthly Loan Transaction Trend',
    labels={'loan_id':'Amount of Transaction','funded_month':'Month'},
    markers=True
)

fig_2.update_traces(line_shape='spline',textposition='top center')

# Summary 3
title_upper = df['title'].str.upper().fillna("")
conditions = [
    title_upper.str.contains('MANAGER|MANAGING|MGR|GM|MNAGER'),
    title_upper.str.contains('OWNER'),
    title_upper.str.contains('OFFICER|ANALYST|SALES|PHYSICIAN|SCIENTIST'),
    title_upper.str.contains('HEAD OF|CHIEF'),
    title_upper.str.contains('SENIOR|SR'),
    title_upper.str.contains('VICE|VP|V. P.'),
    title_upper.str.contains('PRESIDENT|CEO|PRES'),
    title_upper.str.contains('DIRECTOR|COO|CEO|CTO|CFO|EXECUTIVE'),
    title_upper.str.contains('CONSULTANT|ADVISOR')
]

choices = [
    "Manager",
    "Owner",
    "Officer",
    "Head",
    "Senior",
    "Vice President",
    "President",
    "Director",
    "Advisor"
]

df['title_category'] = np.select(conditions,choices,default="Other Worker")
df_funded_title = df.groupby('title_category', as_index=False)['loan_id'].count()

fig_3 = px.pie(
    df_funded_title,
    names='title_category',
    values='loan_id',
    title='Borrower Title Distribution'
)

# Dashboard Layout
app.layout = html.Div([
    # Tambahkan link ke Google Fonts
    html.Link(
        rel='stylesheet',
        href='https://fonts.googleapis.com/css2?family=Poppins&display=swap'
    ),

    # Konten dashboard
    # Header
    html.H1(
        'Loan Luxury Portfolio',
        style={
            'textAlign': 'center',
            'fontFamily': 'Poppins',
            'color': 'black'
            }
        ),

        dcc.Dropdown(
            id='filter-year',
            options=[{'label': y, 'value': y} for y in sorted(df['funded_year'].unique())],
            value=df['funded_year'].max(),
            style={
            'fontFamily': 'Poppins',
            'color': 'black'
            }
        ),

        html.Div([
        dcc.Graph(id='graph-1', figure=fig_1, style={'width':'50%'}),
        dcc.Graph(id='graph-3', figure=fig_3, style={'width':'50%'})
        ],style={'display':'flex'}),

        dcc.Graph(id='graph-2', figure=fig_2)
    ])

# Callback
@app.callback(
    Output('graph-1','figure'),
    Output('graph-2','figure'),
    Output('graph-3','figure'),
    Input('filter-year','value')
)

def filter_year(selected_year):
    filtered_df = df[df['funded_year'] == selected_year]
    
    # Summary 1
    df['funded_amount_mio'] = df['funded_amount'] / 1_000_000
    df_funded_purpose = filtered_df.groupby('purpose', as_index=False)['funded_amount_mio'].sum()

    fig_1 = px.bar(
    df_funded_purpose, 
    x='purpose', 
    y='funded_amount_mio',
    text='funded_amount_mio',
    title='Funded Amount by Loan Purpose',
    labels={'funded_amount_mio':'Funded Amount (in Mio)','purpose':'Loan Purpose'})

    fig_1.update_traces(texttemplate='%{text:.2f}', textposition='outside')


    # Summary 2
    df_funded_monthly = filtered_df.groupby('funded_month', as_index=False)['loan_id'].count()

    fig_2 = px.line(
    df_funded_monthly,
    x='funded_month',
    y='loan_id',
    text='loan_id',
    title='Monthly Loan Transaction Trend',
    labels={'loan_id':'Amount of Transaction','funded_month':'Month'},
    markers=True
    )

    fig_2.update_traces(line_shape='spline',textposition='top center')

    # Summary 3
    df_funded_title = filtered_df.groupby('title_category', as_index=False)['loan_id'].count()

    fig_3 = px.pie(
    df_funded_title,
    names='title_category',
    values='loan_id',
    title='Borrower Title Distribution')

    return fig_1, fig_2, fig_3

# Run local server
if __name__ == '__main__':
    app.run(debug=True)