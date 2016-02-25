
# coding: utf-8


import numpy
import matplotlib
#import pandas as pd
get_ipython().magic(u'pylab inline')
import requests

from bs4 import BeautifulSoup as bs4
from time import sleep

target1 = open("products.txt", 'w')
target2 = open("urls.txt", 'w')

places = ['sfbay','newyork','orlando','rochester','santabarbara','sandiego','springfield','smd','semo','springfieldil','tampa','washingtondc']
for p in places:
    url_base = 'http://'+p+'.craigslist.org/search/sss'
    baseurl = url_base[:url_base.find("org")+3]
    params = dict(lang="en", cc="gb")
    rsp = requests.get(url_base, params=params)

    # BS4 can quickly parse our text, make sure to tell it that you're giving html
    html = bs4(rsp.text, 'html.parser')

    products = html.find_all('a', attrs={'class': 'hdrlnk'})


    for x in products:
        #this_product = products[x]
        target1.write(str(x.contents)+'\n')
        target2.write(baseurl + x.get('href')+'\n')
    sleep(10)
target1.close()
target2.close()

