import spacy
nlp = spacy.load("en_core_web_sm")
file1 = open("sample.txt","r")
text = file1.read()
doc = nlp(text)
sentence_spans = list(doc.sents)
for s in sentence_spans:
        print(s)
        print('-----------------------')
        print('-----------------------')
file1.close()