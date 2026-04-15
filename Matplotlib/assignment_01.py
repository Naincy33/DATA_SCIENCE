import matplotlib.pyplot as plt

# Years
years = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]

# Hypothetical runs
kohli = [800, 900, 850, 950, 1000, 870, 920, 1100, 1050, 980]
rohit = [700, 850, 780, 880, 920, 800, 860, 970, 990, 910]
sehwag = [650, 700, 720, 750, 780, 760, 740, 770, 790, 800]

# Plot lines
plt.plot(years, kohli, label="Kohli", color="blue", linestyle="-")
plt.plot(years, rohit, label="Rohit Sharma", color="green", linestyle="--")
plt.plot(years, sehwag, label="Sehwag", color="red", linestyle=":")

# Labels
plt.xlabel("Years")
plt.ylabel("Runs")

# Title
plt.title("Runs Comparison of Players Over 10 Years")

# Legend
plt.legend()

# Grid
plt.grid()

# Custom style
plt.style.use("ggplot")

# Layout fix
plt.tight_layout()

# Show plot
plt.show()