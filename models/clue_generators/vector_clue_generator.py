from .clue_generator_base import ClueGeneratorBase

import gensim.downloader

class VectorClueGenerator(ClueGeneratorBase):
    def __init__(self, model_name):
        self._keyed_vectors = gensim.downloader.load(model_name)

    def generate_clue(self, pos_words, neg_words):
        clue_pos_neg_diff = dict()

        for clue in list(self._keyed_vectors.index_to_key):
            if not self._is_valid_clue(clue, pos_words):
                continue

            max_neg = max([ self._similarity(clue, neg) for neg in neg_words ])
            min_pos = min([ self._similarity(clue, pos) for pos in pos_words ])
            clue_pos_neg_diff[clue] = min_pos - max_neg
        
        sorted_clues = sorted(list(clue_pos_neg_diff.keys()), key=clue_pos_neg_diff.get, reverse=True)
        top_clue = sorted_clues[0]
        return top_clue.upper()


    def _similarity(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()

        if word1 not in self._keyed_vectors.key_to_index or word2 not in self._keyed_vectors.key_to_index:
            return 0
        return self._keyed_vectors.similarity(word1, word2)


class Word2VecClueGenerator(VectorClueGenerator):
    def __init__(self):
        super().__init__("word2vec-google-news-300")


class GloveNetClueGenerator(VectorClueGenerator):
    def __init__(self):
        super().__init__("glove-wiki-gigaword-300")