import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Fetch Nifty 50 data for March 2025
stock = yf.Ticker("^NSEI")
data = stock.history(start="2025-03-01", end="2025-03-31")
data.reset_index(inplace=True)  
data['Date'] = data['Date'].dt.date

# Load Excel file
df = pd.read_excel('/content/FIDI.xlsx', usecols=['DATE', 'DII Net', 'FII Net'])
df['DATE'] = df['DATE'].dt.date

# Create subplot with 2 rows (Nifty line + FII/DII bars)
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    vertical_spacing=0.1,
                    subplot_titles=("Nifty 50 Closing Prices - March 2025", "FII vs DII Net Investments"))

# Line chart for Nifty
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'],
                         mode='lines+markers', name='Nifty Close',
                         line=dict(color='blue')), row=1, col=1)

# Bar chart for DII and FII Net
fig.add_trace(go.Bar(x=df['DATE'], y=df['DII Net'], name='DII Net', marker_color='skyblue'), row=2, col=1)
fig.add_trace(go.Bar(x=df['DATE'], y=df['FII Net'], name='FII Net', marker_color='orange'), row=2, col=1)

# Layout adjustments
fig.update_layout(height=700, width=1000, title_text="Nifty 50 & FII/DII Net Investments - March 2025",
                  xaxis2=dict(title='Date'), yaxis=dict(title='Nifty Close'),
                  yaxis2=dict(title='Net Value'), barmode='group', template='plotly_white')

fig.show()