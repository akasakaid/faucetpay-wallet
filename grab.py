import re
import os
import sys
try:
    import requests
    from bs4 import BeautifulSoup as bs
except ImportError:
    sys.exit('- module not installed')


class grab:
    def __init__(self, cookie: str):
        self.cookie = cookie

    def main(self):
        headers = {
            "cookie": self.cookie
        }
        req = requests.get(
            "https://faucetpay.io/page/user-admin/linked-addresses", headers=headers)
        parser = bs(req.text, 'html.parser')
        get_tabel = parser.find(
            'table', attrs={'class': 'table table-hover table-bordered'}).find('tbody')
        writer = open('list_wallet.txt', 'a+')
        for address in get_tabel.findAll('tr'):
            wallet = address.findAll('td')[1].text
            writer.write(wallet + '\n')
        print('- wallet save in list_wallet.txt')


if __name__ == "__main__":
    if not os.path.exists('cookie.txt'):
        print('- insert cookie in cookie.txt')
        open('cookie.txt', 'a+')
        sys.exit()
    cookie = open('cookie.txt', 'r').read()
    if len(cookie) == 0:
        sys.exit('- insert cookie in cookie.txt')
    grab(cookie=cookie).main()
