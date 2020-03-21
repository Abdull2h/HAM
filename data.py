import json
def readData(filename):
    with open(filename) as json_file:
        return json.load(json_file)
        
def storeData(srcvar, filename, storein, cat, *data):
    if storein == 'data':
        list(data)
        srcvar[data[0]]={"pass": data[1], "phone": data[2], "email": data[3]}
    elif storein == 'games':
        return

    with open(filename, 'w') as outfile:
        json.dump(srcvar, outfile)

