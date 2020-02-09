from matplotlib import pyplot as plt
import pandas as pd


plt.style.use('ggplot')

# plt.xkcd()

data = pd.read_csv("data.csv")

ages_x = data["Age"]

py_dev_y = data["Python"]
js_dev_y = data["JavaScript"]
dev_y = data["All_Devs"]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
# fig, ax1 = plt.subplots()
# fig, ax2 = plt.subplots()

ax1.plot(ages_x, py_dev_y, color="#5a7d9a", linewidth=3, label="Python Devs")
ax1.plot(ages_x, js_dev_y, color="#c9cc00", linewidth=3, label="JS Devs")

ax2.plot(ages_x, dev_y, color="#444444", linestyle="--", label="All Devs")


ax1.set_xlabel("Ages")
ax1.set_ylabel("Median Salary (USD)")
ax1.set_title("Median Salary (USD) by Age")
ax1.legend()
ax1.grid(True)

ax2.set_xlabel("Ages")
ax2.set_ylabel("Median Salary (USD)")
ax2.set_title("Median Salary (USD) by Age")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
# ax.set_xticks(ages_x)
plt.show()
