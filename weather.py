import requests


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError('redirection detected')


def main():
    locations = ('Лондон', 'svo', 'Череповец')
    payload = {'nTqm': '', 'lang': 'ru'}
    url_template = 'https://wttr.in/{}'
    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        check_for_redirect(response)
        print(response.text)


if __name__ == '__main__':
    main()
