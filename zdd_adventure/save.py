# -*- coding: utf-8 -*-

import json


def load_data():
    # Opening JSON file
    f = open('player_data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    f.close()
    return data

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)
