from text_processing.search_processing import SearchProcessingLogical, SearchProcessingRank


class Metrics:
    def __init__(self, query, list_filenames):
        self.query = query
        self.all_files = list_filenames
        self.logical = SearchProcessingLogical(self.query, *self.all_files)()
        self.rank = SearchProcessingRank(self.query, *self.all_files)()
        self.rank_query = self.rank[self.query]
        self.logic_query = self.logical[self.query]
        self.a = len(set(self.logic_query).intersection(self.rank_query))
        self.b = len(set(self.rank_query).difference(self.logic_query))
        self.c = len(set(self.logic_query).difference(self.rank_query))
        self.d = len(self.all_files) - self.a - self.b - self.c

    def recall(self):
        return self.a / (self.a + self.c)

    def precision(self):
        return self.a / (self.a + self.b)

    def accuracy(self):
        return (self.a + self.d) / (self.a + self.b + self.d + self.c)

    def error(self):
        return (self.b + self.c) / (self.a + self.b + self.d + self.c)

    def fmeasure(self):
        if (self.precision() != 0 or self.recall() != 0) and self.precision() != self.recall():
            return 2 / ((1 / self.precision()) / (1 / self.recall()))
        elif self.precision() == self.recall():
            return self.precision()
        else:
            return 0

    def middle_metric(self):
        return (self.recall() + self.precision() + self.accuracy() + self.error() + self.fmeasure()) / 5

    def precision_n(self):
        return (self.a + self.c) / (self.a + self.b)

    def __call__(self):
        return {'recall': self.recall(), 'precision': self.precision(), 'accuracy': self.accuracy(),
                'error': self.error(), 'fmeasure': self.fmeasure(), 'middle_metric': self.middle_metric(),
                'precision_n': self.precision_n(), 'list_recall': [recall_el / 10 for recall_el in range(10)],
                'list_precision': [self.precision() for _ in range(10)]}
