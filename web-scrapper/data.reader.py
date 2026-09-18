# A simple script for reading the 'images.json'- file created
# from the guiscraper, when 'save as json'- mode is
# selected.
import json

file = open('images.json','r').read()
print(json.loads(file))
