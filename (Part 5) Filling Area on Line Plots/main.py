import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("./data.csv")
ages_x = data["Age"]
all_devs_y = data["All_Devs"]
py_devs_y = data["Python"]
js_devs_y = data["JavaScript"]

plt.plot(ages_x, all_devs_y, label="All Developers",
         color="#444444", linestyle="--")
plt.plot(ages_x, py_devs_y, label="Python Developers", color="#4387B5")
plt.plot(ages_x, js_devs_y, label="JavaScript Developers", color="#F2D63B")

plt.fill_between(ages_x, py_devs_y, all_devs_y,
                 where=(py_devs_y > all_devs_y),
                 interpolate=True, alpha=0.25, label="Above The Average")


# # # Interpolate explanation from the documents
# interpolate : bool, optional
# This option is only relevant if where is used and the two curves are crossing each other.

# Semantically, where is often used for y1 > y2 or similar. By default, the nodes of the polygon defining the filled region will only be placed at the positions in the x array. Such a polygon cannot describe the above semantics close to the intersection. The x-sections containing the intersection are simply clipped.

# Setting interpolate to True will calculate the actual intersection point and extend the filled region up to this point.

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.legend()

plt.show()
