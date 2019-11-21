
## Assignment 3 
The whole assignment was written and tested with Sublime, Linux Python command line.

Goal:

The goal of this assignment is to get practice with the requests library. We will be making a request out to an open GitHub API endpoint to create a small application. We will be querying for content in repositories along with the languague they are written in.

Please complete the following:

    • The URL endpoint is: https://api.github.com/search/repositories

    • It accepts the following parameters:
        ◦ q: the search query. Note, we have to add “+language:python” or “+language:java” to the end of the query to make the whole parameter. Eg:  q=deepfake+language:python
        ◦ sort: the way to sort the returned results. By default, we will set this to “stars”
        ◦ order: Ascending or Descending sort order. By default, we will set this to “desc”

    • A fully built query will look like:
      https://api.github.com/search/repositories?q=deepfake+language:python&sort=stars&order=desc

Please do the following:

    1. import requests and setup the base url (endpoint)
    2. Ask the user for a) Search Query b) Language to Search in
    3. Either through string concatenation or using a params dictionary, build the parameters to tack on to the end of the base url
    4. Use a POST request with the url and parameters, or a GET request with the final url if you built the url using concatenation, to get a response object.
    5. Display the top 10 description field returned from all the repositories of the query



In this assignment, I used a GET request to receive the contents from the given URL. Later on I put the receiving data into json format. The json file is written in a dictionary format with three levels of data, and the description field I want is located at the second level. 

To obtain the description field I want, I implemented the nested loops to iterate through data. The first level of dictionary containing the data type of int, bool and list. If the key type is a list then I iterate through the list that contain a list of dictionaries in the second level. Another for loop was written to iterate through the keys and values in every single dictionary I iterated from the list. If the key is description and the value is not null then I print the key and value. Everytime one is added to the count variable (initialized as zero), when the description field is found. This allowed me to trace down the counts to terminate the nested loops before reaching ten, and ultimately obtain ten description fields.


 