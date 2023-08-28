# trade-slippage-analysis
Calculate total slippage loss from trades in CSV

This script reads in a CSV file containing details of buy/sell trades, including price, stop loss price, and size. It loops through each row, identifies buy/sell trades, calculates the slippage loss per trade (difference between trade price and stop loss price), and accumulates the total slippage loss and number of occurrences of slippage.

The key steps are:

- Read CSV into Pandas DataFrame
- Convert relevant columns to numeric values
- Initialize variables to track total slippage loss and occurrences 
- Loop through rows and identify buy/sell trades
- For buys, calculate slippage as (stop loss - price) * size
- For sells, calculate slippage as (price - stop loss) * size 
- Accumulate slippage loss and increment counter when slippage > 0
- Print total slippage loss and number of trades with slippage

This provides an automated way to analyze trade execution performance by quantifying total slippage from stop loss levels across a set of trades. The output highlights total slippage costs as well as frequency of slippage occurrences.
