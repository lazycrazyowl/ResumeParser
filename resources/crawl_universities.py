#!/usr/bin/env python

import urllib
import bs4

index_url = "http://www.hao123.com/edu"
req = urllib.urlopen(index_url)
html = req.read()

soup = bs4.BeautifulSoup(html)
edu_container = soup.select("div.edu-container")[0]

links = edu_container.select("td a")
for link in links:
    req = urllib.urlopen(link['href'])
    html = req.read()

    soup = bs4.BeautifulSoup(html)
    container = soup.select("div.t1")[0]

    university_links = container.select("a")
    for university in university_links:
        print university.get_text().encode("utf-8")
