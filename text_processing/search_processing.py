from text_processing.text_indexing import TextsIndexing
from rank_bm25 import BM25Okapi


class SearchProcessingLogical(TextsIndexing):
    def __init__(self, query_input, *args):
        super().__init__(*args)
        self.dict_index_words = self.index_words()
        self.query = query_input

    def __call__(self):
        existing_words_text = [word for word in self.preprocess_text(self.query) if word in self.dict_index_words]
        result_dict = {word: self.dict_index_words[word].keys() for word in existing_words_text}
        return result_dict


class SearchProcessingRank(TextsIndexing):
    def __init__(self, query_input, *args):
        super().__init__(*args)
        self.dict_index_words = self.index_words()
        self.query = query_input

    def __call__(self):
        corpus = list(self.dict_filenames.values())
        bm25 = BM25Okapi(corpus)
        preprocess_query = self.preprocess_text(self.query)
        doc_scores = bm25.get_scores(preprocess_query)
        dict_filenames_index = dict(zip(self.dict_filenames.keys(), doc_scores))
        return {" ".join(preprocess_query): [filename for filename, index in dict_filenames_index.items() if index >= 0.10]}
