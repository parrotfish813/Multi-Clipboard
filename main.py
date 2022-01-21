import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    #Saves what is currently on your clipboard to the key given in the json file
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved")

    #Puts the data at the given key to your clipboard
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist")

    elif command == "list":
        print(data)

    #Prints what whatever is stored in the given key
    elif command == "paste":
        key = input("Enter a key: ")
        print(data[key])

    else:
        print("Unknown Command")
else:
    print("Please only pass 1 command")
