import requests
from bs4 import BeautifulSoup

HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    'Referer': 'https://kolesa.kz/',
    'App-Platform': 'frontend',
    'Origin': 'https://kolesa.kz',
}

def get_html(url: str):
   try:
        response = requests.get(url, headers=HEADERS)
        html = response.text

        return html
   except requests.exceptions.RequestException as e:
        print(e)
        return None
   

def get_car_data(url: str):
    try:
        response = requests.get(url, headers=HEADERS)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        car_data = {
            'title': soup.find('title').text,
            'price': soup.find('div', class_='offer__price').text.strip().replace('\n', ''),
        }

        return car_data
    except requests.exceptions.RequestException as e:
        print(e)
        return None