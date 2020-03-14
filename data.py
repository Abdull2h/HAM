import json
def readData(filename):
    with open(filename) as json_file:
        return json.load(json_file)
'''
def storeData(member, us, pw, phone, umail):
    member[us]={"pass": pw, "phone": phone, "email": umail}
    with open('data.json', 'w') as outfile:
        json.dump(member, outfile)
'''
def storeData(srcvar, filename, storein, cat, *data):
    if storein == 'data':
        list(data)
        srcvar[data[0]]={"pass": data[1], "phone": data[2], "email": data[3]}
    elif storein == 'posts':
        return

    with open(filename, 'w') as outfile:
        json.dump(srcvar, outfile)

