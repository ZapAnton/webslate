import urllib.request

url = 'https://pl.bab.la/slownik/polski-rosyjski/'

if __name__ == '__main__':
    with urllib.request.urlopen(url) as response:
        htlm = response.read()

        print(htlm)
