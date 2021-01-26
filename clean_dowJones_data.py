from get_dowJones_data import get_dowJones_data

# define the stock names for the analysi
stock_names = ['^DJI', 'GS', 'MCD', 'DOW', 'CAT', 'MRK', 'CVX', 'VZ', 
          'MSFT', 'AMGN', 'CSCO', 'BA', 'PG', 'JPM', 'WBA', 'DIS',
          'KO', 'MMM', 'AXP', 'WMT', 'JNJ', 'HON', 'V', 'NKE',
          'AAPL', 'CRM', 'HD', 'TRV', 'UNH', 'INTC', 'IBM']

# get dow jones data, using custom class
Gatherer = get_dowJones_data()
dfDowjones_returns = Gatherer.get_stock_data(stock_names, returns=True)
dfDowjones_returns.to_csv("DowJones_Returns.csv")