import json

def loadData():
    d = json.load(open('data.json'))
    return d

def getDefinition(collection, key):
    if key in collection:
        return collection[key]
    else:
        return 0

if __name__ == "__main__":
    data = loadData()
    while True:
        word = input('Please type the word: (press Enter / type Stop to stop the program): ')
        if not word  or word =='Stop':
            print('Exiting the program!')
            break
        else:
            result = getDefinition(data,word.lower().strip())
            if result == 0:
                print('Word doesn\'t exist')
                continue
            else:
                for i in result:
                    print(i)