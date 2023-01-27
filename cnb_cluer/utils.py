from cnb_cluer.models.vector_cluer import Word2VecCluer, GloveNetCluer
from cnb_cluer.models.gpt.simple_cluer import SimpleCluer
from cnb_cluer.models.gpt.simple_neg_cluer import SimpleNegCluer
from cnb_cluer.models.gpt.cot_cluer import CoTCluer
from cnb_cluer.models.gpt.relation_cot_cluer import RelationCoTCluer
from cnb_cluer.models.gpt.simple_reversed_cluer import SimpleReversedCluer
from cnb_cluer.models.gpt.concept_cot_cluer import ConceptCotCluer
from cnb_cluer.models.gpt.concept_cot_reversed_cluer import ConceptCotReversedCluer
from cnb_cluer.models.sampler_cluer.sampler_cluer import SamplerCluer

def get_clue_giver(name):
    if name == "word2vec":
        return Word2VecCluer()
    elif name == "glove":
        return GloveNetCluer()
    elif name == "gpt-simple":
        return SimpleCluer()
    elif name == "gpt-simple-reversed":
        return SimpleReversedCluer()
    elif name == "gpt-simple-neg":
        return SimpleNegCluer()
    elif name == "gpt-cot":
        return CoTCluer()
    elif name == "gpt-relation-cot":
        return RelationCoTCluer()
    elif name == "gpt-concept-cot":
        return ConceptCotCluer()
    elif name == "gpt-concept-cot-reversed":
        return ConceptCotReversedCluer()
    elif name == "sampler":
        return SamplerCluer()
    raise ValueError()