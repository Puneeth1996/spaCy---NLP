
import spacy

nlp = spacy.load("en_core_web_sm")
# Construction 1
doc = nlp("Some text")

# Construction 2
from spacy.tokens import Doc
words = ["hello", "world", "!"]
spaces = [False, True, True]
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc)



# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)