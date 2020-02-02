import random
import pandas as pd
from matplotlib import pyplot as plt

print(plt.style.available)

plt.style.use("seaborn")

data = pd.read_csv("./data.csv")
xs = data["view_count"]
ys = data["likes"]
colors = data["ratio"]


plt.scatter(xs, ys, c=colors, cmap="summer",
            edgecolors="black", s=100, linewidths=1)

plt.xscale("log")
plt.yscale("log")

plt.title("Trending YouTube Videos")
plt.xlabel("View Count")
plt.ylabel("Likes")


cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")


plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()


# xs = [random.randint(1, 9) for i in range(20)]
# ys = [random.randint(1, 9) for i in range(20)]
# colors = [random.randint(1, 9) for i in range(20)]


# # colors = [random.randint(1, 9) for i in range(20)]


# plt.scatter(xs, ys, s=100, c=colors, cmap="summer",
#             edgecolors="black", linewidth=1)
