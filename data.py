import json
def readData():
    with open('data.json') as json_file:
        return json.load(json_file)
members = readData()
def storeData(us, pw, phone, umail):
    members[us]={"pass": pw, "phone": phone, "email": umail}
    with open('data.json', 'w') as outfile:
        json.dump(members, outfile)