import requests
from bs4 import BeautifulSoup
import csv 


url = "https://www.heritageoilltd.com/"
response = requests.get(url=url)

if response.status_code == 200:
    print("Webpage fetched successfully!")

soup = BeautifulSoup(response.text, "html.parser")

print("Webpage Title:", soup.title.string)
links = soup.find_all('h2')
for link in links:
    print(link.get('href'))

with open("articles.csv", "w", newline="", encoding= "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])

    for article in links:
        title = article.text.strip()  # Get the title text
        # Find the <a> tag inside the <h2> and get the 'href' attribute
        link_tag = article.find('a')

        if link_tag and link_tag.get('href'):
            link = link_tag.get('href')
            writer.writerow([title, link])  # Write the title and link to the CSV file
        else:
            print(f"No link found for article: {title}")
print("Articles saved to articles.csv")