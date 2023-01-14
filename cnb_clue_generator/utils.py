from cnb_clue_generator.models.vector_clue_generator import Word2VecGlueGenerator, GloveNetClueGenerator
from cnb_clue_generator.models.gpt_simple_clue_generator import GPTSimpleClueGenerator

def get_model(name):
    if name == "word2vec":
        return Word2VecGlueGenerator()
    elif name == "glove":
        return GloveNetClueGenerator()
    elif name == "gpt-simple":
        return GPTSimpleClueGenerator()
    raise ValueError()