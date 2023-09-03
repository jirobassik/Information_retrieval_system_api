from functools import reduce

from text_processing.text_indexing import TextsIndexing


class SearchProcessing(TextsIndexing):
    def __init__(self, query, *args):
        super().__init__(*args)
        self.dict_index_words = self.index_words()
        self.query = query

    def __call__(self):
        existing_words_text = [word for word in self.preprocess_text(self.query) if word in self.dict_index_words]
        # print('existing words', existing_words_text)
        results = [self.dict_index_words[word].keys() for word in existing_words_text]
        # print(results)
        result_dict = {word: self.dict_index_words[word].keys() for word in existing_words_text}
        # print('dict result', result_dict)
        docs = reduce(lambda x, y: x & y, results) if results else []
        # print('and sort', docs)
        return result_dict


# a = SearchProcessing('programming, dictionary, ', "text1.txt", "text2.txt", "text3.txt")
# a()