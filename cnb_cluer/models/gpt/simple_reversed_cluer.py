from .gpt_cluer import GPTCluer

class SimpleReversedCluer(GPTCluer):
    def generate_clue(self, pos_words, neg_words):
        pos_words = list(reversed(pos_words))
        pos_words_str = self._list_to_str(pos_words)
        prompt = f"Give a single-word clue that is related to {pos_words_str}:"
        completion = self._completer._get_completion(prompt)
        clue = self._format_clue(completion)
        return clue, self._completer.get_history()
