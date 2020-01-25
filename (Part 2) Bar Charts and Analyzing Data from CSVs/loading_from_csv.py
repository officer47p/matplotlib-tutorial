import csv
from matplotlib import pyplot as plt
from collections import Counter

csv_file = open("./data.csv", "r")
csv_reader = csv.DictReader(csv_file)

counter = Counter()

for row in csv_reader:
    counter.update(row["LanguagesWorkedWith"].split(";"))

print(counter)

languages_x = []
popularity_y = []

for item in counter.most_common(15):
    languages_x.append(item[0])
    popularity_y.append(item[1])

languages_x.reverse()
popularity_y.reverse()

plt.barh(languages_x, popularity_y)

# # My own way
# counter_items = list(counter.items())
# counter_items.sort(key=lambda item: item[1])

# languages_x = [item[0] for item in counter_items]
# popularity_y = [item[1] for item in counter_items]

# for lang, pop in zip(languages_x, popularity_y):
#     plt.barh([lang], [pop], label=lang)


# plt.legend()
plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.tight_layout()
plt.show()
