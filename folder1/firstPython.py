
import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to crawl
url = "https://www.goodlifefitness.com/member-details.html#classes"

# Make a request to the website
response = requests.get(url)

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

    print("CJP means Ayega Modi")

else:
    print("Ayega to Modi")
