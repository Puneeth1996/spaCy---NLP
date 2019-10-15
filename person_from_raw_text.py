import spacy
from spacy.tokens import Span
nlp = spacy.load("en_core_web_sm")
file1 = open("sample.txt","r")
text = file1.read()
doc = nlp(text)
print('Names:')
false_values = ['Lender','Blvd','Borrowers','Borrower','Del Rio S','S. Sepulveda Blvd.','Torrance','Hawthorne','P. C. ','JOINTTENANTS','La Mirada','Woodward Ave','GRISELDA ACOSTA7108 MAYFLOWER A','Sioux Falls','Deborah West Roth Living Trust','Deborah West Roth']
# lets try printing on the names in from the samples text files



# doc.ents = [Span(doc, 43, 76, label="PERSON")]
for entity in doc.ents:
        if(entity.label_ == "PERSON") & (entity.text not in false_values):
                print(entity.text,entity.start_char,entity.end_char)


file1.close()