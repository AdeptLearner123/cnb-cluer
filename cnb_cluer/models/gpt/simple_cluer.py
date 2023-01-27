from .gpt_cluer import GPTCluer

class SimpleCluer(GPTCluer):
    def generate_clue(self, pos_words, neg_words):
        pos_words_str = self._list_to_str(pos_words)
        prompt = f"Give a single-word clue that is related to {pos_words_str}:"
        completion = self._completer._get_completion(prompt)
        clue = completion.strip().strip(".").upper()
        return clue, self._completer.get_history()
