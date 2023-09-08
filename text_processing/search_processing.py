from text_processing.text_indexing import TextsIndexing


class SearchProcessing(TextsIndexing):
    def __init__(self, query, *args):
        super().__init__(*args)
        self.dict_index_words = self.index_words()
        self.query = query

    def __call__(self):
        existing_words_text = [word for word in self.preprocess_text(self.query) if word in self.dict_index_words]
        result_dict = {word: self.dict_index_words[word].keys() for word in existing_words_text}
        return result_dict
