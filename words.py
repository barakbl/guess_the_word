import re, random
import requests
from bs4 import BeautifulSoup
import os

class wordsBase:
    def __init__(self, source=None, title=None):
        self.MIN_WORD_LENGTH = 3
        self.source_text = ""
        self.source = source
        self.title = title
        self.load_source()
        self.parse_text()

    def parse_text(self):
        regex = r"([a-zA-Z]{" + str(self.MIN_WORD_LENGTH) + ",})"
        words_list = re.findall(regex, self.source_text)

        ## dict for unique values, and then into list
        self.words = [w for w in {i.lower() for i in words_list}]

    def load_source(self):
        self.source_text = ""

    def get_word(self):
        l = len(self.words)
        return self.words.pop(random.randint(0, l - 1))


class wordsFromFile(wordsBase):
    def load_source(self):
        with open(self.source, "r", encoding="utf-8") as f:
            self.source_text = f.read()

class wordsfromUrl(wordsBase):
    def load_source(self):
        r = requests.get(self.source)
        soup = BeautifulSoup(r.content, "html.parser")
        title = soup.select("title")[0].text
        self.title = f"from: {title}"
        self.source_text = soup.select("body")[0].text


class wordsFromWikipediaRandom(wordsfromUrl):
    def __init__(self):
        super().__init__(source="https://en.wikipedia.org/wiki/Special:Random")


if __name__ == "__main__":
    w = wordsFromFile(source=os.path.abspath("resources/words.txt"))
    print(w.get_word())
    print(len(w.words))
