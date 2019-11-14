
## Assignment 2 
The whole assignment was written and tested with Sublime, Linux Python3 command line.

Pandas amd matplotlib.pyplot libraries are required to be installed on linux before running the program.

Goal:

We are going to use the pandas library to analyze a dataset, very similar to what we did in class. Please feel free to explore the pandas documentation to take the analysis further and learn how the library works and can help you analyze any data you come across in your own work

Please complete the following:

    • Go to www.gapminder.org/data/ and download the ‘Life Expectancy’ data as a csv file. Make sure the csv and your .py file you’re working on are in the same folder, or make sure you file path is correct when importing the csv.

    • Import pandas and use the library to analyze the following questions:

    1. How many rows and columns does this data set have?
    2. What years does the data span?
    3. For the oldest year and the newest year, what are the following summary statistics: mean, std, min, max, 25% quartile, 50% quartile, 75% quartile?
    4. What were the min and max values for South Africa over these years?
    5. What years were these min and max values in (For South Africa)?
    6. As of 2018 which country has the highest and lowest life expectancy?
    7. In the oldest year we have, how many countries had a life expectancy over 50 years old?
    8. In the newest year, how many countries had a life expectancy over 50 years old?

    • Finally, plot a United States vs Germany graph to see interesting trends. What could cause this?



In this assignment, I implemented  13 lambda functions with one regular function. I tried to make every function simple with one line. For question 1, I integrated the method of shape learnt from numpy in class, and I added 1 more row and column in the end, because the header and index_col were skipped. For question 3, I used the slice method learnt from first lecture to slice out the first row "count" from the statistic report, because the question was not asking about it. For question 3, 7 and 8, I looked up the max and min values from the first row of years in the chart and assigned to "newest year" and "oldest year" variables instead of directly taking inputs of 1800 and 2018. It makes more sense to code like this, because we would not know the range of years without looking into the csv file. For question 8, I used list comprehension to iterate through the conditional dataframe, and lastly obtained the length of filtered list.   

I interpreted the plot as a concave up graph, except for some specific years having dramatically decrease in population for Germany and United States. It is probably due to some historical events, WW2, as what I am guessing. In overall, it is convincing to have life expectancy to increase as the advanced of medical technology by times.   
