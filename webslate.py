import urllib.request
from html.parser import HTMLParser

url = 'https://pl.bab.la/slownik/polski-rosyjski/'

def fetch_html_page(word: str):
    with urllib.request.urlopen(url) as response:
        html = response.read()

        return html.decode('utf-8')

class TranslateSiteParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

        self.is_div_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            self.is_div_tag = True

    def handle_endtag(self, tag):
        if tag == 'div' and self.is_div_tag:
            self.is_div_tag = False

    def handle_data(self, data):
        if self.is_div_tag:
            print(data)

if __name__ == '__main__':
    word = 'język'

    html = fetch_html_page(word)

    html_parser = TranslateSiteParser()

    html_parser.feed(html)

    html_parser.close()

