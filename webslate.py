import urllib.request

url = 'https://pl.bab.la/slownik/polski-rosyjski/'

def fetch_html_page(word: str):
    with urllib.request.urlopen(url) as response:
        htlm = response.read()

        print(htlm)

if __name__ == '__main__':
    word = 'język'

    print(fetch_html_page(word))
