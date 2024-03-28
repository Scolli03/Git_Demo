import requests


response = requests.get('https://api.torn.com/faction/?selections=crimes,positions&key=2UQSejH3OfK8S5ne')

responsejson = response.json()

for key in responsejson:
    print(key)


