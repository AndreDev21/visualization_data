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