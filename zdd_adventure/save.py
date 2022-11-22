# -*- coding: utf-8 -*-
import json
import os
path = os.path.dirname(os.path.abspath(__file__))


def load_data():
    # Opening JSON file
    for f in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        print(f)
    f = open(path + '/player_data.json')

    # returns JSON object as a dictionary
    data = json.load(f)
    f.close()
    return data

def load_player_data(name):
    # Opening JSON file
    f = open(path + '/player_data.json')

    # returns JSON object as a dictionary
    data = json.load(f)
    f.close()
    data2 = data[name]
    return data2

def save_data(data):
    ld = load_data()
    ld[data["name"]] = data
    with open(path + '/player_data.json', 'w') as f:
        json.dump(ld, f)
        
def create_new_player(name):
    data = {}
    data["name"] = name
    game_over(data)

def game_over(data1):
    name = data1["name"]
    data = {}
    data["name"] = name
    data["inventory"] = [
        "Studierendenausweis"
    ]
    data["floor"] = -1
    data["room"] = 1
    data["visited_rooms"] = []
    save_data(data)
    return data