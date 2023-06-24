# API link
# https://itunes.apple.com/search?entity=song&limit=1&term=weezer


# The API URL will let us download a text file with JSON formatted string


import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))

for record in response.json()['results']:
    print(record['trackName'])