import json
import os

def check_file():
    if not os.path.exists("store.json"):
        with open("store.json", "w") as f:
            json.dump({}, f, indent=4)

def write(key: str, value):
    check_file()
    with open("store.json") as file:
        decoded = json.load(file)
    
    decoded[key] = value

    with open("store.json", "w") as file:
        json.dump(decoded, file, indent=4)

def view(key: str):
    check_file()
    with open("store.json") as file:
        decoded = json.load(file)

    if decoded:
        try:
            return decoded[key]
        except KeyError:
            return False
    else:
        return False

def check_signup(username):
    with open("store.json") as file:
        decoded = json.load(file)

    for item in decoded:
        if item == username:
            return True
        else:
            continue
        
    return False