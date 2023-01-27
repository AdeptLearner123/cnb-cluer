import random

from .guesser_base import GuesserBase

class VoteGuesser(GuesserBase):

    def __init__(self, num_votes, guesser):
        super().__init__()
        self._num_votes = num_votes
        self._guesser = guesser
    
    def guess(self, words, clue, num):
        votes = { word: 0 for word in words}
        guesses_list = []

        for _ in range(self._num_votes):
            words_shuffled = words.copy()
            random.shuffle(words_shuffled)
            guesses, _ = self._guesser.guess(words_shuffled, clue, num)
            print("Guessing", guesses)

            guesses_list.append(guesses)

            for guess in guesses:
                if guess in votes:
                    votes[guess] += 1
        
        votes_dict = votes
        votes = [ (vote_count, word) for word, vote_count in votes.items() ]
        votes = sorted(votes, reverse=True)
        sorted_words = [ word for _, word in votes ]
        guesses = sorted_words[:num]
        return guesses, {
            "votes": votes_dict,
            "guesses": guesses_list
        }
    
    def get_usage(self):
        self._guesser.get_usage()