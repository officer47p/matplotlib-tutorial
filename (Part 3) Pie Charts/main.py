from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use("fivethirtyeight")


counter = Counter()
data = pd.read_csv("./data.csv")
languages = data["LanguagesWorkedWith"]

for language_list in languages:
    counter.update(language_list.split(";"))

# print(counter)

most_commons = counter.most_common(5)
languages_label = [item[0] for item in most_commons]
popularity_slices = [item[1] for item in most_commons]
# explode = [if i == languages_label.index("Python") 0.1 else 0 for i in range(len(languages_label))]
explode = [0 for i in range(len(languages_label))]
explode[languages_label.index("Python")] = 0.1

plt.pie(popularity_slices, labels=languages_label,
        shadow=True, explode=explode,
        wedgeprops={"edgecolor": "black"},
        autopct="%1.1f%%", startangle=90)

plt.title("My Awesome Pie Plot")
plt.show()
