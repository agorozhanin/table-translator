import requests

BASE_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_course_roubles_to_dollars():
    json = requests.get(BASE_URL)
    dict_data = dict(json.json())
    return dict_data.get('Valute').get('USD').get('Value')
