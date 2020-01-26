from matplotlib import pyplot as plt


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 4]
player2 = [0, 0, 1, 1, 1, 2, 2, 2, 2]
player3 = [1, 1, 1, 2, 2, 2, 2, 2, 3]

labels = ["player1", "player2", "player3"]

plt.stackplot(minutes, player1, player2, player3,
              labels=labels)


plt.title("My Awesome Stack Plot")
plt.xlabel("Minutes")
# We don't need y label, it kinda doesn't make sense :)
# plt.ylabel("Kills")
plt.legend(loc="upper left")
plt.show()
