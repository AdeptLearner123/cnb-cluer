from .gpt_clue_generator_base import GPTClueGeneratorBase

class GPTSimpleClueGenerator(GPTClueGeneratorBase):
    def __init__(self):
        super().__init__()

    
    def generate_clue(self, pos_words, neg_words):
        pos_words_str = ", ".join([ word.upper() for word in pos_words ])
        neg_words_str = ", ".join([ word.upper() for word in neg_words ])
        prompt = f"Give a single-word clue that is related to {pos_words_str} but not {neg_words_str}:"
        completion = self._get_completion(prompt)
        clue = completion.strip().strip(".").upper()
        return clue