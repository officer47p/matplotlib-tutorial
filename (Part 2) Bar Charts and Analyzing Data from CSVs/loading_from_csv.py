import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

# print(plt.style.available)
plt.style.use("fivethirtyeight")

with open("./data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    first_row = next(csv_reader)

    c = Counter(first_row["LanguagesWorkedWith"].split(";"))
    for row in csv_reader:
        c.update(row["LanguagesWorkedWith"].split(";"))

    names_x = list(c.keys())
    plt.bar(names_x, [c[f"{name}"] for name in names_x])
    plt.show()
