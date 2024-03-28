import requests
from pprint import pprint
from datetime import datetime

response = requests.get('https://api.torn.com/faction/?selections=crimes,positions&key=2UQSejH3OfK8S5ne')

responsejson = response.json()

crimes = responsejson['crimes']

for key in crimes:

    if crimes[key]['time_left'] > 0:
        print(datetime.fromtimestamp(int(crimes[key]['time_ready'])))




