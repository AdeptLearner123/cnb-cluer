from abc import ABC, abstractmethod

class GuesserBase(ABC):
    @abstractmethod
    def guess(self, words, clue, num):
        pass

    
    def get_usage(self):
        return {}