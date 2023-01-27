from ..cluer_base import Cluer
from .gpt_completer import GPTCompleter

class GPTCluer(Cluer):
    def __init__(self):
        self._completer = GPTCompleter()
    
    def get_usage(self):
        self._completer.get_usage()
    
    def _list_to_str(self, words):
        words = [ self._format_word(word) for word in words ]
        return ", ".join(words[:-1]) + " and " + words[-1]
    
    def _format_word(self, word):
        return f"\"{word.lower()}\""
    
    def _format_clue(self, clue):
        return clue.strip().strip(".\"").upper()