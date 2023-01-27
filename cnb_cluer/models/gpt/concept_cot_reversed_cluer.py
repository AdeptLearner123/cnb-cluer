from .gpt_cluer import GPTCluer

class ConceptCotReversedCluer(GPTCluer):
    def generate_clue(self, pos_words, neg_words):
        pos_words = list(reversed(pos_words))
        pos_words_str = self._list_to_str(pos_words)
        prompt = \
                f"Find a concept that is related to {pos_words_str}:"
        completion = self._completer._get_completion(prompt)

        prompt2 = prompt + completion + f"\n\nFind a single-word clue that is related to {pos_words_str}:"
        completion2 = self._completer._get_completion(prompt2)

        clue = self._format_clue(completion2)
        return clue, {
            "prompt": prompt2,
            "completion": completion2
        }