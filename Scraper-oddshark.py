#!/usr/bin/python3

# fetch data from oddshark.com and print as CSV

import simplejson as json
import urllib.request
import urllib.parse
import datetime
import sys

def fetch(daynum):
  # get yesterday's date (always use yesterday)
  yesterday = datetime.datetime.now() - datetime.timedelta(days = daynum)
  url = 'http://io.oddsshark.com/scores/nhl/' + yesterday.strftime("%Y-%m-%d")

  # make it look like a browser. these are from Firefox on Linux.
  headers = {
    'Origin'          : 'http://www.oddsshark.com',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'en-US,en;q=0.9',
    'User-Agent'      : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.132 Chrome/63.0.3239.132 Safari/537.36',
    'Accept'          : '*/*',
    'Referer'         : 'http://www.oddsshark.com/nhl/scores',
    'Connection'      : 'keep-alive'
  }

  # create request
  req = urllib.request.Request(url, headers=headers)

  # read response
  with urllib.request.urlopen(req) as response:
    jdata = response.read()

  # translate json from response into structure
  pjson = json.loads(jdata)

  # loop throug the games in the response and print:
  # - home team name
  # - home team scores by period (joined by '-')
  # - home team moneyline value
  # - away team name
  # - away team scores by period (joined by '-')
  # - away team moneyline value
  # - total (like '5.5' (whatever that is))
  #
  for j in pjson:
    # get list of scores per period
    shome = ''
    saway = ''
    for seg in j['segments']:
      shome += seg['home_points'] + '-'
      saway += seg['away_points'] + '-'
    shome = shome[:-1] # remove last hyphen
    saway = saway[:-1] # remove last hyphen

    # now print everything, joined by commas
    print(','.join((
      # home team
      j['home_name'], shome, j['home_money_line'],
      # away team
      j['away_name'], saway, j['away_money_line'],
      # total
      j['total']
    )))

days = 2
if len(sys.argv) == 2:
  days = sys.argv[1]

for day in range(1, int(days) + 1):
  fetch(day)
