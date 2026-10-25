
#  import requests
import urllib.request
import urllib
from bs4 import BeautifulSoup
import csv

# Define the URL to crawl
url = "http://clubs.html"
response = urllib.request.urlopen(url)
html = response.read()
html_string = html.decode("utf-8")
print(html_string)


# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    # Print the URLs of the links
    # for link in links:
    #    print(link.get('href'))

    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))

    with open("links.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Links"])
        for link in links:
            writer.writerow([link])

    print("Links saved to clubsAndSchedules.csv file")

else:
    print("Request failed")
    print("Ayega Modi jobhi Ukhad na hai Ukhadlo")
