from ..cluer_base import Cluer
from ..vector_cluer import GloveNetCluer
from ..gpt.cot_cluer import CoTCluer
from ..gpt.simple_cluer import SimpleCluer
from .vote_guesser import VoteGuesser
from .gpt_guesser import ListGuesser

import random
from collections import Counter

class SamplerCluer(Cluer):
    
    def __init__(self):
        self._cluers = [ GloveNetCluer(), CoTCluer(), SimpleCluer() ]
        self._guesser = VoteGuesser(5, ListGuesser())
    
    def generate_clue(self, pos_words, neg_words):
        #clues = [ cluer.generate_clue(pos_words, neg_words) for cluer in self._cluers ]
        clues = []
        for cluer in self._cluers:
            clue, _ = cluer.generate_clue(pos_words, neg_words)
            print("Generating clue", clue)
            clues.append(clue)

        
        print("Clues:", clues)
        clues = set(clues)
        clue_results = dict()

        words = pos_words + neg_words
        random.shuffle(words)
        for clue in clues:
            guess, notes = self._guesser.guess(words, clue, len(pos_words))
            clue_results[clue] = notes
    
        clue_scores = { clue: self._evaluate_clue(pos_words, neg_words, clue_results[clue]["votes"]) for clue in clues }
        best_clue = max(clue_scores, key=clue_scores.get)
        return best_clue, clue_results

    def _evaluate_clue(self, pos_words, neg_words, votes):
        min_pos_vote = min([ votes[word] for word in pos_words ])
        max_neg_vote = max([ votes[word] for word in neg_words ])
        return min_pos_vote - max_neg_vote
    
    def get_usage(self):
        usage = sum([ Counter(cluer.get_usage()) for cluer in self._cluers ], Counter(self._guesser.get_usage()))
        return dict(usage)