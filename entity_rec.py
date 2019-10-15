import spacy
nlp = spacy.load("en_core_web_sm")

text = ("""Apple is looking at buying U.K. startup for $1 billion""")
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