from .guesser_base import GuesserBase
from ..gpt_completer import GPTCompleter

class GPTGuesser(GuesserBase):
    def __init__(self):
        self._completer = GPTCompleter()
    

    def get_instruction(self, words, clue, num):
        words_str = ", ".join(words)

        return \
            f"Find the {num} words from the given words that are most related to the given clue.\n\n" + \
            f"Words: {words_str}\n" + \
            f"Clue: {clue}\n"
    
    def process_answer(self, answer):
        guesses = answer.strip().split(", ")
        guesses = [guess.upper() for guess in guesses]
        return guesses
    
    def print_usage(self):
        self._completer.print_usage()


class GPTSimpleGuesser(GPTGuesser):
    def guess(self, words, clue, num):
        prompt = self.get_instruction(words, clue, num) + \
                "Related words (comma-separated):"
        
        completion = self._completer._get_completion(prompt)
        return self.process_answer(completion), prompt + completion


class GPTCoTGuesser(GPTGuesser):
    def guess(self, words, clue, num):
        prompt = self.get_instruction(words, clue, num) + \
                "Let's think step-by-step."
        
        completion = self._completer._get_completion(prompt)

        prompt2 = prompt + completion + "\n\n" +\
            "Related words (comma-separated):"
        
        print(prompt2)
        completion2 = self._completer._get_completion(prompt2)
        return self.process_answer(completion2), prompt2 + completion2


class GPTListGuesser(GPTGuesser):
    def guess(self, words, clue, num):
        prompt = self.get_instruction(words, clue, num) + "\n" + \
                f"First let's see why {clue} might be related to each of the given words."
        
        completion = self._completer._get_completion(prompt)

        prompt2 = prompt + completion + "\n\n" +\
            "Answer (comma-separated):"
        
        print(prompt2)
        completion2 = self._completer._get_completion(prompt2)
        return self.process_answer(completion2), prompt2 + completion2
