import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

df = pd.read_csv('../Datasets/constituents-financials_csv.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['Name']).agg(
    {'Price/Earnings': 'sum', 'Price/Book': 'sum', 'Market Cap': 'sum'}).reset_index()

# Preparing data
data = go.Scatter(x=new_df['Price/Earnings'],
                  y=new_df['Price/Book'],
                  text=new_df['Name'], mode='markers',
               marker=dict(size=new_df['Market Cap'] / 10000000000,color=new_df['Market Cap'] / 100, showscale=True))

# Preparing layout
layout = go.Layout(title='S&P 500 Companies', xaxis_title="Price to Earnings Ratio",
                   yaxis_title="Price/Book")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')
