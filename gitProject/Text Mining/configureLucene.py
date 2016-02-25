import spotlight
import os
from createLuceneIndex import *

products = open("products.txt", "r")
urls = open("urls.txt", "r")

for x in range(0, 1200):
    product = products.readline()
    url = urls.readline()
    createind(product,url)