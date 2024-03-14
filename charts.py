import matplotlib.pyplot as plt
import pandas as pd
import main


bank_data = main.bank_data

########################
#Create a Python boxplot
########################
# df_transposed = main.bank_data.transpose()

# Create boxplot
# plt.figure(figsize=(10, 6))
# plt.boxplot(df_transposed.values.T, labels=df_transposed.index)  # Transpose data for correct plotting
# plt.xlabel('Stocks Prices')
# plt.ylabel('Bank')
# plt.title('Boxplot of Bank Stock Prices (5Y Lookback)', fontsize = 20)
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# plt.tight_layout()  # Adjust layout to prevent clipping of labels
# plt.show()





########################
#Create a Python scatterplot
########################

#Set the size of the matplotlib canvas
# plt.figure(figsize = (18,12))

# #Create the x-axis data
# dates = bank_data.index.to_series()
# dates = [pd.to_datetime(d) for d in dates]

# #Create the y-axis data
# WFC_stock_prices =  bank_data['WFC']

# #Generate the scatterplot
# plt.scatter(dates, WFC_stock_prices)

# #Add titles to the chart and axes
# plt.title("Wells Fargo Stock Price (5Y Lookback)", fontsize=20)
# plt.ylabel("Stock Price", fontsize=20)
# plt.xlabel("Date", fontsize=20)




# ########################
# #Create a Python histogram
# ########################

# #Set the size of the matplotlib canvas
# plt.figure(figsize = (18,12))

# #Generate the histogram
# plt.hist(bank_data.transpose(), bins = 50)

# #Add a legend to the histogram
# plt.legend(bank_data.columns,fontsize=20)

# #Add titles to the chart and axes
# plt.title("A Histogram of Daily Closing Stock Prices for the 5 Largest Banks in the US (5Y Lookback)", fontsize = 20)
# plt.ylabel("Observations", fontsize = 20)
# plt.xlabel("Stock Prices", fontsize = 20)
# plt.show()

################################################
################################################
#Create subplots in Python
################################################
################################################

########################
#Subplot 1
########################
plt.subplot(2,2,1)

#Generate the boxplot
plt.boxplot(bank_data.transpose())

#Add titles to the chart and axes
plt.title('Boxplot of Bank Stock Prices (5Y Lookback)')
plt.xlabel('Bank', fontsize = 20)
plt.ylabel('Stock Prices')

#Add labels to each individual boxplot on the canvas
ticks = range(1, len(bank_data.columns)+1)
labels = list(bank_data.columns)
plt.xticks(ticks,labels)

########################
#Subplot 2
########################
plt.subplot(2,2,2)

#Create the x-axis data
dates = bank_data.index.to_series()
dates = [pd.to_datetime(d) for d in dates]

#Create the y-axis data
WFC_stock_prices =  bank_data['WFC']

#Generate the scatterplot
plt.scatter(dates, WFC_stock_prices)

#Add titles to the chart and axes
plt.title("Wells Fargo Stock Price (5Y Lookback)")
plt.ylabel("Stock Price")
plt.xlabel("Date")

########################
#Subplot 3
########################
plt.subplot(2,2,3)

#Create the x-axis data
dates = bank_data.index.to_series()
dates = [pd.to_datetime(d) for d in dates]

#Create the y-axis data
BAC_stock_prices =  bank_data['BAC']

#Generate the scatterplot
plt.scatter(dates, BAC_stock_prices)

#Add titles to the chart and axes
plt.title("Bank of America Stock Price (5Y Lookback)")
plt.ylabel("Stock Price")
plt.xlabel("Date")

########################
#Subplot 4
########################
plt.subplot(2,2,4)

#Generate the histogram
plt.hist(bank_data.transpose(), bins = 50)

#Add a legend to the histogram
plt.legend(bank_data.columns,fontsize=20)

#Add titles to the chart and axes
plt.title("A Histogram of Daily Closing Stock Prices for the 5 Largest Banks in the US (5Y Lookback)")
plt.ylabel("Observations")
plt.xlabel("Stock Prices")

plt.tight_layout()

################################################
#Save the figure to our local machine
################################################

plt.savefig('bank_data.png')