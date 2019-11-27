
## Assignment 4 

The whole assignment is written and tested with Sublime, Linux Python command line. 


In the linux command console, you can run:

### python Assignment4.py


Goal:

The goal of this assignment is to get practice with the BeautifulSoup library and more advanced python concepts that can be applied to scraping. You will make a series of requests to a wallpaper image site to try to download the full-sized wallpapers and save them to your system.

Please complete the following:

•	The URL endpoint is: https://wallhaven.cc/search?categories=100&purity=100&topRange=1y&sorting=toplist&order=desc

•	You will need to make a request to this URL and store the content.

•	Use BeautifulSoup to find all the image thumbnails and the links in them to the final (full-sized) images. Store these in a list to iterate over.

•	Visit each of the full-size image links and use BeautifulSoup to find the final image link (ends with .jpg/.png etc).

•	Make another immediate request to get this content and find the file type/extension using whichever method you find useful.

•	Think of a filename to use (using elements on the page, or just 0, 1, 2... etc) and save the file to your disk with that filename

•	Initally, you should have ~20 wallpapers that downloaded to your system (AJAX requests will grab these on a page by page basis as you “scroll” down the screen”



The assignment is mostly implemented as instructed from class. The only thing that is different:

    Due to version 2.7 python is installed on my machine, I made an if not existed conditional check to verify whether the destination of downloaded pictures is already existed, instead of passing the parameters into the function os.makdir(path, ifexisted). 

Lastly, a folder "Assignment4_Downloaded_Pictures" will be created and storing all the pictures as jpg  file type from the requiring webpage.
