import requests
import  json
import jsonpath

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send Get Request
response = requests.get(url)

# Display Response Content
# print(response.content)
# print(response.headers)

# Parse response to JSON
json_response = json.loads(response.text)
# print(json_response)

# Fetch value useing Json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])