import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import requests
import json
import datetime
import threading
from time import sleep

plt.style.use("seaborn")

# # Guide request_url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD"
request_url = "https://min-api.cryptocompare.com/data/pricemulti?"
coins_parameter = "fsyms"
currencies_parameter = "tsyms"

currencies = ["USD"]
coins_data_list = {"BTC": {"name": "Bitcoin", "prices": []},
                   "ETH": {"name": "Ethereum", "prices": []},
                   "BCH": {"name": "Bitcoin Cash", "prices": []},
                   "BSV": {"name": "Bitcoin SV", "prices": []},
                   "EOS": {"name": "EOS", "prices": []},
                   "ETC": {"name": "Ethereum Classic", "prices": []},
                   "OKB": {"name": "Okex", "prices": []},
                   "LTC": {"name": "Litecoin", "prices": []},
                   "XRP": {"name": "XRP", "prices": []}
                   }
#   {"name": "Binance Coin", "symbol": "BNB"}
coins_list = list(coins_data_list.keys())
# print(coins_list)
time_series = []


def plotter(i):
    global time_series
    global coins_data_list
    print(time_series)
    print(coins_data_list["BTC"]["prices"])
    temp_date = datetime.datetime.now().time().strftime("%H:%M:%S")
    time_series.append(temp_date)
    price_list = requests.get("{}{}={}&{}={}".format(
        request_url, coins_parameter, ",".join(coins_list), currencies_parameter, ",".join(currencies))).json()
    # print(temp_date)
    counter = 0
    # print(price_list.json())

    for row in ax:
        for col in row:
            col.cla()
            current_coin = coins_list[counter]
            coins_data_list[current_coin]["prices"].append(
                price_list[current_coin]["USD"])

            if len(coins_data_list[current_coin]["prices"]) > 20:
                coins_data_list[current_coin]["prices"] = coins_data_list[current_coin]["prices"][-20:]
                time_series = time_series[-20:]

            col.plot(
                time_series, coins_data_list[current_coin]["prices"], label=current_coin)
            col.set_xlabel("Time")
            col.set_ylabel("Price(USD)")
            col.set_title(coins_data_list[current_coin]["name"])
            col.legend()
            fig.autofmt_xdate()
            counter += 1


fig, ax = plt.subplots(nrows=3, ncols=3, sharex=False, sharey=False)

animation = FuncAnimation(fig, plotter, interval=1000)
plt.tight_layout()
plt.grid(True)
plt.show()
