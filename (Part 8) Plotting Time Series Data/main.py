from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd

plt.style.use("seaborn")

data = pd.read_csv("./data.csv")

# Makes the Date column a datetime column so we can sort our date based on that
data["Date"] = pd.to_datetime(data["Date"])
# Sorts our pandas DataFrame based on the "Date" column
data.sort_values("Date", inplace=True)

price_date = data["Date"]
price_close = data["Close"]

plt.plot_date(price_date, price_close, linestyle="solid")

# Rotates the units in our x axis
plt.gcf().autofmt_xdate()

plt.xticks(price_date)

plt.show()
