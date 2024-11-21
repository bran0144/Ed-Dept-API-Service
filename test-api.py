import requests
import json


url = 'http://127.0.0.1:9009/college_search'
data = {'collegeName': "Indiana University Bloomington"}

headers = {'Content-Type': 'application/json'}

response = requests.get(url, json=data, headers=headers)
# print(response.text)
# with open("sample.json", "w") as outfile:
# json.dump(response, outfile)

with open('outputfile2.json', 'wb') as outf:
    outf.write(response.content)