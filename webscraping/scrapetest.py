import urllib2
from bs4 import BeautifulSoup

scape_site = "http://zsaegesser.github.io/"

page = urllib2.urlopen(scape_site)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h1')

name = name_box.text.strip()
print name
