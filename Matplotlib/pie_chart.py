import matplotlib.pyplot as plt

plt.style.use("ggplot")  # Choose any style you like

labels = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs = [18000, 8000, 12000, 9500]
 
plt.title("Career Runs of Indian Batsmen")

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(runs, labels=labels, colors=colors)
plt.show()

plt.pie(
    runs,
    labels=labels,
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': '--'}
)
plt.show()


explode = [0.1, 0, 0, 0]  # Only highlight Sachin's slice

plt.pie(runs, labels=labels, explode=explode, colors=colors)
plt.title("Exploded Pie Example")
plt.show()

plt.pie(
    runs,
    labels=labels,
    explode=explode,
    colors=colors,
    shadow=True  # adds a 3D-like shadow
)
plt.show()

plt.pie(
    runs,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140
)
plt.title("Career Run Share")
plt.show()