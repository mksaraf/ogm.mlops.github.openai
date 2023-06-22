 output

import requests
from bs4 import BeautifulSoup
import googletrans

# get the web page
url = "https://www.example.com"
page = requests.get(url)

# parse the web page
soup = BeautifulSoup(page.content, 'html.parser')

# extract all headers
headers = soup.find_all('h1', 'h2', 'h3', 'h4', 'h5', 'h6')

# create an empty list to store the translated headers
translated_headers = []

# translate the headers
for header in headers:
    translated_header = googletrans.Translator().translate(header.text, dest='es').text
    translated_headers.append(translated_header)

# save the translated headers into an html file
with open('translated_headers.html', 'w') as f:
    for header in translated_headers:
        f.write("<h1>{}</h1>\n".format(header))