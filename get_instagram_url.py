#!/usr/bin/python
import requests
import sys
import json


if len(sys.argv) != 2:
    print('Error! Please, use a photo ID')
    exit()

photo_id = sys.argv[1]
url = 'http://api.instagram.com/oembed?url=http://instagram.com/p/{0}/'
response = requests.get(url.format(photo_id))

if response.status_code != 200:
    print('Error! {0}'.format(response.status_code))
    exit()

json_res = json.loads(response.content)
if 'url' not in json_res.keys():
    print('Error! Bad photo ID or bad response')
    exit()

print(json_res['url'])