# Python program to read the contents of URL
# Importing urllib module
import urllib.request
# Open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://wordpress.org/plugins/about/readme.txt')

# Get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# Read the data from the URL and print it
data = webUrl.read()
print (data)
