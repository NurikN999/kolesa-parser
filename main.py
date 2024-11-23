from bs4 import BeautifulSoup
import requests
import helpers

cities = {
    'алматы': 'almaty',
    'астана': 'astana',
}

url = 'https://kolesa.kz'
city = input('Введите город поиска: ').lower()
city = cities.get(city, 'almaty')
parse_url = f'{url}/cars/{city}'

price_to = int(input('Введите максимальную цену: '))
price_from = int(input('Введите минимальную цену: '))

if price_to != 0 and price_to > price_from:
    parse_url = f'{parse_url}?price[to]={price_to}'
if price_from != 0:
    parse_url = f'{parse_url}?price[from]={price_from}'

html = helpers.get_html(parse_url)
soup = BeautifulSoup(html, 'html.parser')

# Extracting the last page number
last_page = 1
pager = soup.find('div', class_='pager')
if pager:
    page_links = pager.find_all('a')
    if page_links:
        last_page = int(page_links[-2].text)

# Parsing data_id from all pages
for page in range(1, last_page + 1):
    page_url = f'{parse_url}&page={page}'
    html = helpers.get_html(page_url)
    soup = BeautifulSoup(html, 'html.parser')
    
    for item in soup.find_all('div', class_='a-list__item'):
        data_card = item.find('div', class_='a-card')
        if data_card:
            data_id = data_card.get('data-id', 'none')
            data = helpers.get_car_data(f'{url}/a/show/{data_id}')
            print(data.get('title', 'none'))
            print(data.get('price', 'none'))