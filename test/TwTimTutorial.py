from bs4 import BeautifulSoup

with open("resources/index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print (doc)