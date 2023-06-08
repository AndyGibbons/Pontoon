dict = {"this": "that"}

def change_dict(myDict):
    myDict.update({"this": "this"})
    return myDict

dict = change_dict(dict)

print(dict)