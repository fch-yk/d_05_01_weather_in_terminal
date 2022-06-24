import requests


def main():
    locations = ('Лондон', 'svo', 'Череповец')
    payload = {'nTqm': '', 'lang': 'ru'}
    url_template = 'https://wttr.in/{}'
    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
