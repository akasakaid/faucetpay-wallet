import re
import os
import sys
import random
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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "cookie": self.cookie
        }
        req = requests.get(
            "https://faucetpay.io/page/user-admin/linked-addresses", headers=headers)
        open('hasil.html', 'wb').write(req.content)
        if "Dashboard" in req.text:
            parser = bs(req.text, 'html.parser')
            get_tabel = parser.find(
                'table', attrs={'class': 'table table-hover table-bordered'}).find('tbody')
            total_wallet = len(get_tabel.findAll('tr'))
            print('- total wallet address :', total_wallet)

            for address in get_tabel.findAll('tr'):
                wallet = address.findAll('td')[1].text
                unlink_url = re.search(
                    'class="btn btn\-sm btn\-outline\-danger btn\-icon" href="(.*?)"', str(address.findAll("td")[3]).split("<a ")[2]).group(1)
                req = requests.get(
                    unlink_url, headers=headers)
                print('- unlink address ' + wallet)


if __name__ == "__main__":
    if not os.path.exists('cookie.txt'):
        print('- insert cookie in cookie.txt')
        open('cookie.txt', 'a+')
        sys.exit()
    cookie = open('cookie.txt', 'r').read()
    if len(cookie) == 0:
        sys.exit('- insert cookie in cookie.txt')
    try:
        grab(cookie=cookie).main()
    except KeyboardInterrupt:
        sys.exit()
