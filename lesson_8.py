import json

data = '''
[
  { "id" : "1",
    "lang" : "fr",
    "value" : "Bonjour"
  } ,
  { "id" : "2",
    "lang" : "es",
    "value" : "Buenos días"
  },
  { "id" : "4",
    "lang" : "de",
    "value" : "Guten Morgen"
  },
  { "id" : "4",
    "lang" : "pl",
    "value" : "Cześć"
  }
]'''

info = json.loads(data)
print('Items count:', len(info))

for item in info:
    print('Lang', item['lang'])
    print('Value', item['value'])
