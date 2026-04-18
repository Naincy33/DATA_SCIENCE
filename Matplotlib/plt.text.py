import matplotlib.pyplot as plt

players = ["Sachin", "Sehwag", "Kohli"]
runs = [1500, 1200, 1800]

plt.bar(players, runs, color="skyblue")

# Add labels on top of bars
for i in range(len(players)):
    plt.text(i, runs[i] + 50, str(runs[i]), ha='center')

plt.ylabel("Runs")
plt.title("Runs Scored by Players")
plt.tight_layout()
plt.show()