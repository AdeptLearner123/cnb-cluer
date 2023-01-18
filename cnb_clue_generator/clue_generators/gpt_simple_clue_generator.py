from .clue_generator_base import ClueGeneratorBase
from ..gpt_completer import GPTCompleter

class GPTSimpleClueGenerator(ClueGeneratorBase):
    def __init__(self):
        self._completer = GPTCompleter()

    
    def generate_clue(self, pos_words, neg_words):
        pos_words_str = ", ".join([ word.upper() for word in pos_words ])
        neg_words_str = ", ".join([ word.upper() for word in neg_words ])
        prompt = f"Give a single-word clue that is related to {pos_words_str} but not {neg_words_str}:"
        completion = self._completer._get_completion(prompt)
        clue = completion.strip().strip(".").upper()
        return clue
    
    def print_usage(self):
        self._completer.print_usage()