# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
file1 = open("sample_output.txt","r")
text = file1.read()
# print(text)
doc = nlp(text)

# Analyze syntax

# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts

# for entity in doc.ents:
#     print(entity.text, entity.label_)


print('Names:')
# lets try printing on the names in from the samples text files
for entity in doc.ents:
        if(entity.label_ == "PERSON"):
                print(entity.text)


file1.close()
