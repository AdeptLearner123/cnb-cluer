from abc import ABC, abstractmethod

class ClueGeneratorBase(ABC):
    @abstractmethod
    def generate_clue(self, pos_words, neg_words):
        pass
    

    def print_usage(self):
        print("No usage")
    
    
    def _is_valid_clue(self, clue, pos_words):
        return clue.upper() not in pos_words and "_" not in clue.upper() and "-" not in clue.upper() and not any([ pos_word in clue.upper() for pos_word in pos_words ])