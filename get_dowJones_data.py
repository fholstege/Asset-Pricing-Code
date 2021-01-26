# -*- coding: utf-8 -*-

import yfinance as yf
import pandas as pd



class get_dowJones_data:
    """
    get_dowJones_data: used to pull and clean dow jones data from the yahoo finance API
    """
    
    def get_stock_data(self,stock_names,start_date='2019-03-21', end_date='2020-12-31', data_type = 'Adj Close', returns=False):
        """
        get_stock_data: pulls data from a stock in the dow jones index from the yahoo finance api

        Arguments: 
            stock_names; list of stock names to be pulled 
            start_date; string, of format 'YYYY/MM/DD'
            end_date; string, of format 'YYYY/MM/DD'
            data_type; string, type of data to be pulled for stock
            returns; boolean, if true turn to returns instead of raw prices
        """

        # store the data for each stock here
        lStock_data = []

        # go over each stock name
        for stock in stock_names:
            
            # pull data for a stock
            stock_data = yf.download(stock, start=start_date, end=end_date)[data_type]

            # append the stock data to a list
            lStock_data.append(stock_data)
        
        # combine the list of pd.series to a single dataframe
        dfStock_data = pd.concat(lStock_data, axis=1, keys=[i for i in stock_names])
        dfStock_data.columns = stock_names

        if returns:
            # turn metric to  returns
            dfReturn_data = dfStock_data.pct_change()
            dfReturn_data.dropna(inplace=True)

            return (dfReturn_data)
        else:
            return(dfStock_data)


