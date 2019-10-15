import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
file1 = open("sample.txt","r")
text = file1.read()
doc = nlp(text)
pharse_list = ["(B) Borrower is ","(B)Borrower "]
sentence_spans = list(doc.sents)
# Iterate over the sentence list until the sentence end value exceeds a match start value:
for sent in sentence_spans:
    print(sent)
    print(pharse_list)
    if pharse_list[1] in sent:  # this is the fifth match, that starts at doc3[673]
        print(sent)