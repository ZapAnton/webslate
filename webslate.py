from urllib import request, parse
from html.parser import HTMLParser

url = 'https://pl.bab.la/slownik/polski-rosyjski/'

def fetch_html_page(word: str):
    final_url = url + parse.quote(word)

    with request.urlopen(final_url) as response:
        html = response.read()

        return html.decode('utf-8')

class TranslateSiteParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

        self.is_translation_tag = False

        self.translations = []

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'dict-result':
                    self.is_translation_tag = True

                    break

    def handle_endtag(self, tag):
        if tag == 'div' and self.is_translation_tag:
            self.is_translation_tag = False

    def handle_data(self, data):
        if self.is_translation_tag:
            self.translations.append(data)

def write_to_file(html_string: str):
    with open('translate.html', 'w') as file:
        file.write(html_string)

if __name__ == '__main__':
    word = 'język'

    html = fetch_html_page(word)

    write_to_file(html)

    html_parser = TranslateSiteParser()

    html_parser.feed(html)

    html_parser.close()

    print(html_parser.translations)

