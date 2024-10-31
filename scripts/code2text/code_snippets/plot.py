import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', color='b', label="Sample Data")

plt.title("Simple Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.grid(True)
plt.show()