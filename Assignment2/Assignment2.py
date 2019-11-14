import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("life_expectancy_years.csv", index_col = "country")

returnRows = lambda: df.shape[0]+1
returnCols = lambda: df.shape[1]+1
yearsSpan = lambda: df.head(0).columns
findOldestYear = lambda: yearsSpan().max() 
findNewestYear = lambda: yearsSpan().min()
southAfricaMax = lambda: df.loc['South Africa'].max()
southAfricaMin = lambda: df.loc['South Africa'].min()
southAfricaMaxYear = lambda: df.loc['South Africa'].idxmax()
southAfricaMinYear = lambda: df.loc['South Africa'].idxmin()
maxCountry2018 = lambda: df[findOldestYear()].idxmax() 
minCountry2018 = lambda: df[findOldestYear()].idxmin()
over50YearsOldCountriesOld = lambda: len([i for i in df[findOldestYear()][df[findOldestYear()] > 50]])
over50YearsOldCountriesNew = lambda: len([i for i in df[findNewestYear()][df[findNewestYear()] > 50]])

def returnNewandOldStats(oldestYear, newestYear):
	newAndOldStats = df[[oldestYear, newestYear]].describe()
	return newAndOldStats[1::]


print("1. How many rows and columns does this data set have? \n")
print("The data set has " + str(returnRows()) + " rows and " + str(returnCols()) + " columns\n")

print("2. What years does the data span? \n")
print("The years covered by the data set are: " + str(yearsSpan()) + "\n")

print("3. For the oldest year and the newest year, what are the following summary statistics: mean, std, min, max, 25% quartile, 50% quartile, 75% quartile? \n")
print("The summary statistics from the oldest year and newest year are shown as below" + str(returnNewandOldStats(findNewestYear(),findOldestYear())) + '\n')

print("4. What were the min and max values for South Africa over these years? \n")
print("The min and max values for South Africa over years 1800-2019 are " + str(southAfricaMin()) + " and " + str(southAfricaMax()) + "\n")

print("5. What years were these min and max values in (For South Africa)? \n")
print("The years contain min and max values are " + str(southAfricaMinYear()) + " and " + str(southAfricaMaxYear()) + "\n")

print("6. As of 2018 which country has the highest and lowest life expectancy? \n")
print("The country has the lowest life expectancy in 2018 is " + str(minCountry2018()) + "\nThe country has the highest life expectancy in 2018 is " + str(maxCountry2018()) + "\n")

print("7. In the oldest year we have, how many countries had a life expectancy over 50 years old? \n")
print(str(over50YearsOldCountriesOld()) + " countries \n")

print("8. In the newest year, how many countries had a life expectancy over 50 years old? \n")
print(str(over50YearsOldCountriesNew()) + " country \n")

df.loc[['United States','Germany']].T.plot()
plt.xlabel('Year')
plt.ylabel('Years (How many years)')
plt.title("Life Expectancy of United States vs Germany")
plt.show()