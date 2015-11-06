import json

with open('APIKeys.json') as keys_file:    
    data = json.load(keys_file)
    print data