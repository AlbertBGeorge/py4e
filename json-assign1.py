import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter location: ")
connection = urllib.request.urlopen(url)
print('Retrieving', url)
data = connection.read().decode()

js = json.loads(data)

print('Retrieved', len(js), 'characters')

counts = []
comments = js["comments"]

for comment in comments:
    counts.append(comment['count'])    

print("Count: ", len(counts))
print("Sum: ", sum(counts))