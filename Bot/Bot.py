
import misc

import requests

token = misc.token
print(token)

URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates(URL):
    url = URL + 'getupdates'
    r = requests.get(url)
    return r


def main():
    get_updates(URL)


if __name__ == '__main__':
    main()