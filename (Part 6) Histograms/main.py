import pandas as pd
from matplotlib import pyplot as plt

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

data = pd.read_csv("./data.csv")
ages = data["Age"]

plt.hist(ages, bins=bins, edgecolor="black")

# The average age of all respondents
median_age = 29

# Drawing the average age line on the plot
plt.axvline(median_age, color="orange", label="Average age of all respondents")

plt.title("Ages Of Responders")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")
plt.xticks(bins)
plt.legend()

plt.show()
