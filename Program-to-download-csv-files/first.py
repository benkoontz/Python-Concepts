# program to build a web crawler

from urllib import request

goog_url = 'http://samplecsvs.s3.amazonaws.com/TechCrunchcontinentalUSA.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url) # stores connection to webpage
    csv = response.read() # read data from url
    csv_str = str(csv) # converts data to string
    lines = csv_str.split("\\n") # split takes long string and breaks in up when it goes to a newline
    dest_url = r'amazon.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)
