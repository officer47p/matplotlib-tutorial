import numpy as np
from matplotlib import pyplot as plt
# Link to format string in matplotlib Docs: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html


# Printing all the themes
print(plt.style.available)

# Styling the figure
plt.style.use('ggplot')

# A cool theme for making our figure more like a hand drawing
# plt.xkcd()

bar_width = 0.2

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.array(ages_x)

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
# This method uses formatted strings
# plt.plot(ages_x, dev_y, "k--", label="All Devs")
plt.bar(x_indexes - bar_width, dev_y, width=bar_width,
        color="#444444", label="All Devs")


# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# This method uses formatted strings
# plt.plot(ages_x, py_dev_y, "b", label="Python Devs")
plt.bar(x_indexes, py_dev_y, width=bar_width,
        color="#5a7d9a",  label="Python Devs")


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes + bar_width, js_dev_y, width=bar_width,
        color="#c9cc00", label="JS Devs")


plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")


# First method of adding legends
# plt.legend(["All Devs", "Python Devs"])

# This one only activates the passed labels to the plot method
plt.legend()

# margin problem in the figure window (for example when I use other themes for my figure, I face some margin problem)
plt.tight_layout()

# Adding grid to our plot
plt.grid(True)

# Showing all the x values (ages here)
plt.xticks(ages_x)

# To save a plot programmatically
# plt.savefig("./plot.png")

# Showing the plot
plt.show()
