import requests
import json

formulas = [1, 3, 6, 2]
query = {'name': 'new', 'formulas': json.dumps(formulas)}
# print(json.dumps(query))
print(requests.post('http://127.0.0.1:5000/api/v2/collections', query).text)