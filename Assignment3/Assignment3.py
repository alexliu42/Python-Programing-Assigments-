import requests
import json

endPoint= \
"https://api.github.com/search/repositories"

query = raw_input("Search Query:")
language = raw_input("Language to search in:")
fullQuery = query + "+language:" + language

p = { "q":fullQuery.lower(), "sort": "stars", "order": "desc"}

response = requests.get(endPoint, params=p)

count = 0

if response.status_code == 200:
	json = response.json()  			     	#convert response into json file
	print("Top 10 descriptions are:")
	for k, v in json.items():					#iterate through items to get to the list
		if type(v) == list:
			for i in v:							# iterate through a list of dictionary  
				for k1, v1 in i.items():  		#iterate through items in the nested dictionary		
					if count == 10:				# break the loops when it reaches 10 descriptions
						break
					elif k1 == "description" and v1 is not None: 	 #print the items if key is "description" and when the value is not equal to NULL
						count += 1
						print("%s : %s" % (k1, v1))   #print out keys and values in strings
						