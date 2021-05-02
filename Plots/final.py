# @author Harsh Patel, Andrew Martino, Jessica Cochran, and Mir Mansoor Khan
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/constituents-financials_csv.csv')
app = dash.Dash()

# edit start

# single line S&P500
# Load CSV file from Datasets folder
df2 = pd.read_csv('../Datasets/SP500.csv')
df2['Date'] = pd.to_datetime(df2['Date'])

# Preparing data
data_single = [go.Scatter(x=df2['Date'], y=df2['SP500'], mode='lines', name='Death')]

# multi line s&p500
# Load CSV file from Datasets folder
df3 = pd.read_csv('../Datasets/Gold Silver Dow.csv')
df3['Date'] = pd.to_datetime(df3['Date'])

# Preparing data
trace1 = go.Scatter(x=df3['Date'], y=df3['Gold'], mode='lines', name='Gold')
trace2 = go.Scatter(x=df3['Date'], y=df3['Silver'], mode='lines', name='Silver')
trace3 = go.Scatter(x=df3['Date'], y=df3['Dow'], mode='lines', name='Dow')
data_multi = [trace1,trace2,trace3]

# edit end

app.layout = html.Div(children=[
    html.H1(children='Magic Return',
            style={
                'textAlign': 'center',
                'color': '#df1e56',
                'font-weight': 'bold',
                'font-size': '36px'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Easy-to-use Stock Analysis using Investing Basics', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H2('Why Invest in the Stock Market?', style={'color': '#df1e56', 'font-size': '30px'}),
    html.Div("Let’s assume that we can all agree that it's important to save money for the future. And one manages to save $1,000. Now let's put it under your mattress, but when you come to get it, even years later, you’ll still be left with the same $1,000 you put there in the first place. It won’t grow at all. In fact, the rise in the prices of things will make that same $1,000 worth less. This is called Inflation and it is the biggest reason why one should consider investing."),
    html.Br(),
    html.Div("But why the Stock Market? The primary benefit of investing in the stock market is for a chance to grow your money. The stock market has created an enormous amount of wealth over the years. On average, the S&P 500 which consists of 500 of the largest U.S. publicly traded companies has returned 8% to 12% per year. At that rate, only $10,000 invested in the stock market 50 years ago would have grown into more than $380,000 today."),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_single,
                  'layout': go.Layout(title='S&P 500 From 1950 to 2018', xaxis_title="Year",
                   yaxis_title="Price (USD)")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('What about Investing in Gold and Silver?', style={'color': '#df1e56', 'font-size': '30px'}),
    html.Div("Many investors seek out gold and silver in physical forms with the hopes for their value to rise in the future due to the limited supply of these precious metals. But investing in gold and silver is not as easy as buying a stock of a company. There is the headache of storing and selling physical gold and silver, and gold does not earn dividends like many blue chip stocks."),
    html.Br(),
    html.Div("How does Gold compare against the S&P 500? Gold has underperformed by quite a bit compared to the S&P 500 over this period, with the S&P index generating nearly a 100% in total returns compared to gold, which returned just 42.5% over the same period."),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multi,
                  'layout': go.Layout(title='Value of Gold, Silver, Dow Jones Industrial Average From 1968 to 2019', xaxis_title='Year',
                  yaxis_title='Price (USD)')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('What stocks should I Invest in?', style={'color': '#df1e56', 'font-size': '30px'}),
    html.Div("The most important thing to know about investing in individual stocks is: “Most people have no business investing in individual stocks on their own”. That’s right, it's so important you might as well read it again. Most individual investors lose money investing in individual stocks."),
    html.Br(),
    html.Div("Choosing individual stocks without any idea of what you’re looking for is like running through a dynamite factory with a burning match. You may live, but you’re still an idiot. (Joel Greenblatt)", style={'textAlign': 'center', 'font-style': 'italic', 'margin-left': '20%', 'margin-right': '20%'}),
    html.Br(),
    html.Div("For most, investing in index funds like S&P 500 is the way to go. But for those looking to get higher than average return on their investment comparative to the market there is a proven strategy. Magic formula investing is simple and easy to use long-term strategy for value investing. The strategy was developed by investor and hedge fund manager Joel Greenblatt. Here’s how it works: "),
    html.Br(),
    html.Div("1. Paying a bargain price when you purchase a share in a business is a good thing. One way to do this is to purchase a business that earns more relative to the price you are paying rather than less. In other words, a higher earnings yield is better than a lower one.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("2. Buying a share of a good business is better than buying a share of a bad business. One way to do this is to purchase a business that can invest its own money at high rates of return rather than purchasing a business that can only invest at lower ones. In other words, businesses that earn a high return on capital are better than businesses that earn a low return on capital.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("3. Combining points 1 and 2, buying good businesses at bargain prices is the Magic Formula.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.H3('Analyze individual stocks using Magic Formula here:', style={'color': 'grey', 'font-size': '20px'}),
    dcc.Graph(id='graph1'),
    html.Div('Please select a sector', style={'color': 'grey', 'margin': '18px', 'font-weight': 'bold'}),
    dcc.Dropdown(
        id='select-sector',
        options=[
            {'label': 'Health Care', 'value': 'Health Care'},
            {'label': 'Information Technology', 'value': 'Information Technology'},
            {'label': 'Consumer Discretionary', 'value': 'Consumer Discretionary'},
            {'label': 'Utilities', 'value': 'Utilities'},
            {'label': 'Financials', 'value': 'Financials'},
            {'label': 'Materials', 'value': 'Materials'},
            {'label': 'Real Estate', 'value': 'Real Estate'},
            {'label': 'Consumer Staples', 'value': 'Consumer Staples'},
            {'label': 'Energy', 'value': 'Energy'},
            {'label': 'Telecommunication Services', 'value': 'Telecommunication Services'},
        ],
        value='Information Technology'
    ),
    html.Br(),
    html.H3('Instructions on how to use the above chart:', style={'color': '#df1e56'}),
    html.Div("1. Select a sector of companies that you are interested in.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("2. The bubble/circle represents the individual stocks of different companies in the selected sector.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("3. The y-axis represents the EBITDA or how good the company is towards generating profits from its assets. Higher is better.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("4. The x-axis represents the Price-to-earnings ratio that represents if stock price is a bargain compared to its earnings. Lower is better.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("5. The size of the bubble/circle represents the market capitalization of the company. Or how big the company is.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("6. And the color on the bubble represents dividend yield. Dividend yield is percent of profits paid-out by company inrelation to stock price. Higher is better.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div("7. Use a combination of these factors to determine your preferred stock.", style={'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.Div('Disclaimer: Our content is intended to be used and must be used for information and education purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances. You should take independent financial advice from a professional in connection with, or independently research and verify, any information that you find on our Website and wish to rely upon, whether for the purpose of making an investment decision or otherwise. The data provided on this website is not up-to-date with current stock market.', style={'textAlign': 'center', 'font-size': 10, 'margin-left': '10%', 'margin-right': '10%'}),
    html.Br(),
    html.Div('Created by: Andrew Martino, Harsh Patel, Jessica Cochran, and Mir Mansoor Khan (Group-23)', style={'textAlign': 'center', 'font-weight': 'bold'}),
    html.Br(),
    html.Br(),
    html.Br()

])
# Layout

@app.callback(Output('graph1', 'figure'),
              [Input('select-sector', 'value')])
def update_figure(selected_sector):
    filtered_df = df1[df1['Sector'] == selected_sector]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    new_df = filtered_df.groupby(['Name']).agg(
        {'Price/Earnings': 'sum', 'EBITDA': 'sum', 'Market Cap': 'sum', 'Dividend Yield': 'sum'}).reset_index()

    data_interactive_bubblechart = [go.Scatter(x=new_df['Price/Earnings'],
                                              y=new_df['EBITDA'],
                                              text=new_df['Name'], mode='markers',
                                              marker=dict(size=new_df['Market Cap'] / 10000000000,
                                                          color=new_df['Dividend Yield'], showscale=True, colorbar=dict(title="Dividend Yield %")))]

    layout = go.Layout(title='S&P 500 Companies in ' + selected_sector, xaxis={'title': 'Price/Earnings'},
                                                                            yaxis={'title': 'EBITDA'})

    return {'data': data_interactive_bubblechart, 'layout': layout}


if __name__ == '__main__':
    app.run_server()

