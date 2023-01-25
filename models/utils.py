from cnb_clue_generator.clue_generators.vector_clue_generator import Word2VecClueGenerator, GloveNetClueGenerator
from cnb_clue_generator.clue_generators.gpt_simple_clue_generator import GPTSimpleClueGenerator
from cnb_clue_generator.guessers.vector_guesser import Word2VecGuesser, GloveNetGuesser
from cnb_clue_generator.guessers.gpt_guesser import GPTSimpleGuesser, GPTCoTGuesser, GPTListGuesser
from cnb_clue_generator.guessers.gpt_relation_guesser import GPTRelationGuesser
from cnb_clue_generator.guessers.gpt_few_shot_guesser import GPTFewShotGuesser

def get_clue_giver(name):
    if name == "word2vec":
        return Word2VecClueGenerator()
    elif name == "glove":
        return GloveNetClueGenerator()
    elif name == "gpt-simple":
        return GPTSimpleClueGenerator()
    raise ValueError()