import spacy
nlp = spacy.load("en_core_web_sm")

text = ("""Sir Charles Spencer Chaplin KBE was an English comic actor, filmmaker, and composer who rose to fame in the era of silent film. He became a worldwide icon through his screen persona, "The Tramp", and is considered one of the most important figures in the history of the film industry.""")
doc = nlp(text)
# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
print('\n----')

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
    print('\n----')


for chunk in doc.noun_chunks:
    print('\n')
    print(chunk.text)
    print('\n')