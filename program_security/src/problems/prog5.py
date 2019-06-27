# This example shows how to use Python with JSON

import json

def storeJSON(fileName, data = {}):
    fd = open(fileName, 'w')
    json.dump(data, fd, indent = 4, separators = (',', ': '))

def loadJSON(fileName):
    fd = open(fileName)
    data = json.load(fd)
    print(data)
    return data

if __name__ == '__main__':
    data = loadJSON('example.json')
    print(data['menu']['value'])
    data['menu']['value'] = 'movie'
    storeJSON('example.json', data)
    loadJSON('example.json')
    print(data['menu']['value'])
