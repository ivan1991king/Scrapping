#TASK 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json
USER = "ivan1991king"
GIT_API_URL = 'https://api.github.com'
response = requests.get(GIT_API_URL + '/users/' + USER + '/repos')
#информация по репозиториям в формате JSON
data = json.loads(response.text)
with open('HW1_my_repos.json', 'w') as outfile:
    json.dump(data, outfile)
print(*(repo['name'] for repo in data), sep='\n')

# TASK 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к
# нему, пройдя авторизацию. Ответ сервера записать в файл.¶
# Сайт last.fm/api

LASTFM_API_URL = ' http://ws.audioscrobbler.com/2.0/'
API_KEY = '4286c74653144313ac14dcfc8dae161a'

PARAMS = {'method': 'artist.gettoptracks',
          'artist': 'Red Hot Chili Peppers',
          'api_key': API_KEY,
          'format': 'json'}
response = requests.get(LASTFM_API_URL, params=PARAMS)
data =json.loads(response.text)
with open('HW1_RHCP_toptracks.json', 'w') as outfile:
    json.dump(data, outfile)
for i in range(5):
    print(data['toptracks']['track'][i]['name'])