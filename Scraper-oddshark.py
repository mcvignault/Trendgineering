#!/usr/bin/python3

import simplejson as json
import urllib.request
import urllib.parse

url = 'http://io.oddsshark.com/scores/nhl/2018-01-23'

headers = {
  'Origin'          : 'http://www.oddsshark.com',
  'Accept-Encoding' : 'gzip, deflate',
  'Accept-Language' : 'en-US,en;q=0.9',
  'User-Agent'      : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.132 Chrome/63.0.3239.132 Safari/537.36',
  'Accept'          : '*/*',
  'Referer'         : 'http://www.oddsshark.com/nhl/scores',
  'Connection'      : 'keep-alive'
  }

# d = {}
data = urllib.parse.urlencode({})
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
print(req)

with urllib.request.urlopen(req) as response:
  data = response.read()

# print(data)

json = json.dumps(data)
print(json)
