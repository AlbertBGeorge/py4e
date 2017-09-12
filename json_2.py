import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]''' 
#Use this triple quoted string to add the json key value pairs.
#The curly braces have to lined up properly.

info = json.loads(data) #Converts the above json into a sructred complex.
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
