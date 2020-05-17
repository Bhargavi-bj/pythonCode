# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:25:17 2020

@author: Bharghavi
"""

import requests
import json

def get_pokemon_data(name="pikachu"):
    url = "https://api.pokemontcg.io/v1/cards?name={}".format(name)
    response = requests.get(url)
    return response.json()

pokemon_name = input("Enter the name of the pokemon:")
recieved_data = get_pokemon_data(pokemon_name)
#print(recieved_data['cards'])

import matplotlib.pyplot as plt

url_data = requests.get(recieved_data['cards'][1]['imageUrl'])
with open('./pika.png','wb') as f:
    for item in url_data.iter_content(1024):
        f.write(item)
    
image_data = plt.imread('./pika.png')
plt.imshow(image_data)
plt.show()


