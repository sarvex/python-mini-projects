import requests as rq
from bs4 import BeautifulSoup

url = input("Enter Link: ")
data = rq.get(url) if ("https" or "http") in url else rq.get(f"https://{url}")
soup = BeautifulSoup(data.text, "html.parser")
links = [link.get("href") for link in soup.find_all("a")]
# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
with open("myLinks.txt", 'a') as saved:
    print(links[:10], file=saved)
