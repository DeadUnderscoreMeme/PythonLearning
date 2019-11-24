import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    if state["Location"] == "North":
        del state["Name"]
        del state["Abbreviation"]
        del state["Location"]

with open('noNorth.json','w') as f:
    json.dump(data, f, indent= 2)
