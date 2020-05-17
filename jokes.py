# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:46:57 2020

@author: Bharghavi
"""

import requests

url = "https://sv443.net/jokeapi/category/programming?blacklistFlags=nsfwpolitical"



response = requests.get(url)
recieved_data = response.json()
#print(response.text.encode('utf8'))
#print(response)
#print(recieved_data)
for x in recieved_data.keys():
    if x == 'id' or x == 'warning':
        continue
    print("{} : {}".format(x, recieved_data[x]))
    #print(recieved_data[x])
 
 
 
 