import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ---------------- Task 1 ----------------
# Line plot of a simple list
data = [10, 20, 15, 25, 30]

plt.figure(figsize=(6,4))
plt.plot(data, marker='o')
plt.title("Line Plot")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()

# ---------------- Task 2 ----------------
# Area plot of cumulative data
values = [5, 10, 15, 20, 25]
cumulative = pd.Series(values).cumsum()

plt.figure(figsize=(6,4))
plt.fill_between(range(len(cumulative)), cumulative)
plt.plot(cumulative, marker='o')
plt.title("Area Plot")
plt.xlabel("Index")
plt.ylabel("Cumulative Values")
plt.show()

# ---------------- Task 3 ----------------
# Violin plot using Seaborn
tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot")
plt.show()
