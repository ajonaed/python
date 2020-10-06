import json
from difflib import *
def loadData():
    d = json.load(open('data.json'))
    return d

def getDefinition(collection, key):
    if key in collection.keys():
        return collection[key]
    elif key.title() in collection.keys():
        return collection[key.capitalize()]
    elif key.upper() in collection.keys():
        return collection[key.capitalize()]
    # elif key.title() in collection:
    #     return collection[key]
    else:
        return None

def getMatches(collection, key):
    if get_close_matches(key.lower(),collection.keys(),3,1):
        for i in collection[key.lower()]:
            print(i)
        #print(collection[key.lower()])
        return 1
    else:
        return get_close_matches(key,collection.keys(),3,0.8)


if __name__ == "__main__":
    data = loadData()
    while True:
        word = input("Please type the word: (press Enter to stop): ")
        if not word  or word =='Stop':
            print('Exiting the program!')
            break
       # elif:
        else:
            result = getDefinition(data,word.strip())
            if not result :
                closeMatches = getMatches(data, word)
                if closeMatches == 1:
                    #result = getDefinition(data,word.lower())
                    continue
                elif not closeMatches:
                    print('Word doesn\'t exist')
                    continue
                else:
                    print(closeMatches, 'Did you mean any of these words?')
                    continue
            for i in result:
                    print(i)