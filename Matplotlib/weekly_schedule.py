import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

studying = [4,5,3,4,5,2,3]
gym = [1,1,1,1,1,0,0]
mobile = [2,3,2,3,2,4,5]
sleep = [7,6,7,6,7,8,8]

labels = ['Studying', 'Gym', 'Mobile', 'Sleep']
colors = ['skyblue', 'lightgreen', 'orange', 'lightcoral']

plt.figure(figsize=(10,6))

plt.stackplot(days, studying, gym, mobile, sleep,
              labels=labels, colors=colors, alpha=0.8)

plt.legend(loc='upper left')
plt.title('Choti Weekly Routine 😎')
plt.xlabel('Day (1 = Monday)')
plt.ylabel('Hours')

plt.grid()
plt.tight_layout()

plt.show()