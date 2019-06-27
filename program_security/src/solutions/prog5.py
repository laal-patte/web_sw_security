# This example shows how to use Python with JSON

import json

def storeJSON(fileName, data = {}):
    try :
        fd = open(fileName, 'w')
        json.dump(data, fd, indent = 4, separators = (',', ': '))
    except :
        print('file',fileName,'not found')

def loadJSON(fileName):
    try :
        fd = open(fileName)
        data = json.load(fd)
        print(data)
        return data
    except :
        print('file',fileName,'not found')

if __name__ == '__main__':
    try :
        data = loadJSON('example.json')
        print(data['menu']['value'])
        data['menu']['value'] = 'movie'
        storeJSON('example.json', data)
        loadJSON('example.json')
        print(data['menu']['value'])
    except :
        print('unable to load')

#solution: use try except when opening files or using data from files
