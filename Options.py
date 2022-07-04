from pickle import FALSE
import re
from tkinter.messagebox import YES
import yfinance as yf
import time
from datetime import datetime

while True:
    try:
        print("")
        ticker = input("Please Enter A Ticker Name: ")
        print("")

        stock = yf.Ticker(ticker)

        # Gets stock ticker
        print(stock.ticker,"|",stock.info['currency'] )
        print("")
        break
    except:
        print("ERROR: Not A Valid Ticker Name.")

        



# Business Summary
print(stock.info['longBusinessSummary'])
print("")

# Stock information function
def stockinfo():
    stock = yf.Ticker(ticker)
    print("Stock Price:", stock.info['regularMarketPrice'])
    print("Stock Volume:", stock.info['regularMarketVolume'])
    print("Market Open Price:", stock.info['open'])
    print("Previous Close Price:", stock.info['regularMarketPreviousClose'])
    print("52 Week High:", stock.info['fiftyTwoWeekHigh'])
    print("52 Week Low:", stock.info['fiftyTwoWeekLow'])
    print("")
stockinfo()

#Gets stock holder info
print("Stock Holder Information:")
print(stock.major_holders)
print("")

#Gets stock sustainability
print("Stock Sustainability:")
print(stock.sustainability)
print("")

#Shows Option Expiry Dates
print("Option Expiry Dates:")
print("")
print(stock.options)
print("")

# Verify if the Option Expiry Date is valid

while True:
    try:
        date = input("Please Enter A Option Expire Date (Year-MM-DD): ")
        option_chain = stock.option_chain(date)       
        break
    except Exception as e:
        print("")
        print(e)
        print("")

print("")

# Options information function
def options():
    # gets Options Information
    print("Options Information:")
    print("")
    print("Calls:")
    print(option_chain.calls.sort_values('lastTradeDate'))
    print("")
    print("Puts:")
    print(option_chain.puts.sort_values('lastTradeDate'))
    print("")
options()

# Sets refresh to zero to allow the refresh to happen until the program is exited
refresh = 0

while refresh == 0:
    # Updates the Stock Price and Options data every 15 seconds.
    time.sleep(15)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("")
    print("")
    print("------------------------------------------------------")
    print("")
    print("Information Updated At: ", current_time)
    stockinfo()
    options()
    print("------------------------------------------------------")