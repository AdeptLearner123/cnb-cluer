from .gpt_cluer import GPTCluer

class CoTCluer(GPTCluer):
    def generate_clue(self, pos_words, neg_words):
        pos_words_str = ", ".join([ word.upper() for word in pos_words ])
        neg_words_str = ", ".join([ word.upper() for word in neg_words ])
        prompt = \
                f"Give a single-word clue that is related to {pos_words_str} but not {neg_words_str}:\n\n" +\
                "Let's think about this step by step."
        completion = self._completer._get_completion(prompt)

        prompt2 = prompt + completion + "\n\nClue:"
        completion2 = self._completer._get_completion(prompt2)

        clue = completion2.strip().strip(".").upper()
        return clue, {
            "prompt": prompt2,
            "completion": completion2
        }
