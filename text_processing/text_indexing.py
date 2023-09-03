import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from pathlib import Path
from string import punctuation


class TextsIndexing:
    def __init__(self, *args):
        self.__filenames = args
        self.__dict_filenames = {}

    def create_dict_texts(self):
        for filename in self.filenames:
            # print('preprocess text', self.preprocess_text(self.reading_file(filename)))
            self.__dict_filenames[filename] = self.preprocess_text(self.reading_file(filename))

    def preprocess_text(self, text_input: str):
        text = self.remove_quotes(text_input).lower()
        return self.remove_stopwords_punct(text)

    @staticmethod
    def reading_file(filename: str):
        return Path("media", filename).read_text()

    def index_words(self):
        self.create_dict_texts()
        dict_index_words = {}
        for filename, list_words in self.dict_filenames.items():
            for index, word in enumerate(list_words):
                dict_index_words.setdefault(word, {})[filename] = index
        return dict_index_words

    @staticmethod
    def remove_stopwords_punct(text: str):
        stop_words = set(stopwords.words("english"))
        return [
            word
            for word in word_tokenize(text)
            if word not in stop_words and word not in punctuation
        ]

    @staticmethod
    def remove_quotes(text: str) -> str:
        return re.sub('"', "", text)

    @property
    def filenames(self):
        return self.__filenames

    @property
    def dict_filenames(self):
        return self.__dict_filenames
