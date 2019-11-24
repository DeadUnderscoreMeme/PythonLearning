import json

month = '''
{
    "Months" : [{
    "1":"January",
    "2":"February",
    "3":"March",
    "4":"April",
    "5":"May",
    "6":"June",
    "7":"July",
    "8":"August",
    "9":"September",
    "10":"October",
    "11":"November",
    "12":"December"
    }]
}
'''

data = json.loads(month)

for month in data["Months"]:
    del month["2"]

data2 = json.dumps(data, indent = 2)

print(data2)

