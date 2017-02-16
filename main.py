from my_lib import get_html
from bs4 import BeautifulSoup as BS
import os


def get_pages(html):
    try:
        pages = BS(html, 'lxml').find_all('span', class_='page')[-2].text
        return int(pages)
    except AttributeError:
        return 1


def parsing(html, obj):
    soup = BS(html, 'lxml')
    r = soup.find('td', {'valign':'top', 'style':'width: 100%;'}).find_all('td', class_='header')
    for i in r:
        soup = BS(get_html(f"http://soft.sibnet.ru{i.find('a').get('href')}", 'cp1251'), 'lxml')
        name = soup.find('h1', itemprop='name').text.strip()

        print(name )


def main(ob):

    obj, os = ob
    url = f'http://soft.sibnet.ru/search/?text={obj.strip()}&os={os.strip()}&&pg=1'
    pages = get_pages(get_html(url, 'cp1251'))
    for i in range(1, 2):
        base_url = f'http://soft.sibnet.ru/search/?text={obj.strip()}&os={os.strip()}&&pg={i}'
        parsing(get_html(base_url, 'cp1251'), obj)



if __name__ == '__main__':
    print(f'{"-" * 50:^{100}}')
    print(f'{"Введите через запятую (что ищем,os)":^{100}}')
    print(f'{"os = 0-Все, 1-Windows, 2-unix, 10-Android":^{100}}')
    print(f'{"-" * 50:^{100}}')
    main(input('Что ищем:').split(','))