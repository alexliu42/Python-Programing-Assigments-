import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Cars.csv", index_col = "Title")

df.loc["Price"] = df.loc["Price"].str.strip("$")

df.loc["Price"]= df.loc["Price"].astype(float)

df.loc["Price"].plot.hist(bins=20)

plt.xlabel("Price")
plt.title("Price of cars on Craigslist on %s" %df.loc["Date"][1])
plt.show()
