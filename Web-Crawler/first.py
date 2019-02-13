# program to build a web crawler

import requests # used for connecting from the internet to get information from webpages
from bs4 import BeautifulSoup # module that lets you go a website and sort through data

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url) # requests data from website
        plain_text = source_code.text # take the text of the request and store it in plain text
        soup = BeautifulSoup(plain_text) # beautiful needs the data sorted in a cetain way
        # loop through all source code and pick out links
        for link in soup.findAll('a', {'class': 'item-name'}): # find all of a specific item, a is link for anchors
            href = "https://buckysroom.org" + link.get('href') # get the text in the href attribute
            title = link.string # print title of every item
            print(href)
            print(title)
            get_single_item_data(href)
        page += 1

# function to get each item individually
def get_single_item_data(item_url):
    source_code = requests.get(item_url)  # requests data from website
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div' ,{'class' : 'i-name' }):
        print(item_name.string)
    # gather links from individual pages
    for link in soup.findAll('a'):
        href = "https://bucksroom.org" + link.get('href')
        print(href)


trade_spider(1) # search 1 page
