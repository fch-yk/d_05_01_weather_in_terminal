import requests


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError('redirection detected')


def main():
    url = 'https://wttr.in/san%20francisco?nTqu&lang=en'
    response = requests.get(url)
    response.raise_for_status()
    check_for_redirect(response)
    print(response.text)


if __name__ == '__main__':
    main()
