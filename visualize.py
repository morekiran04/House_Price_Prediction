import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("House Price India.csv")

plt.scatter(df['area'], df['price'])

plt.title("House Price vs Area")
plt.xlabel("Area")
plt.ylabel("Price")
plt.grid(True)

plt.show()