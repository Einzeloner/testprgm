# Regression in python 

# imports 
import pandas as pd
import quandl

table = quandl.get('WIKI/GOOGL')

# The raw unfiltered data
print(table.head())

# making the list 

table = table[['Adj. Open', 'Adj. High', 'Adj. Close', 'Adj. Volume', 'Adj. Low']]

table['HL-pct'] = (table['Adj. High'] - table['Adj. Close']) / table['Adj. Close'] * 100.0
table['PCT-change'] = (table['Adj. Close'] - table['Adj. Open']) / table['Adj. Open'] * 100.0

table = table[['Adj. Close', 'HL-pct', 'PCT-change', 'Adj. Volume']]

# Just with the useful things 
print(table.head())
