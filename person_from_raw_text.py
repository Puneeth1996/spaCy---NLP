import spacy
nlp = spacy.load("en_core_web_sm")
file1 = open("sample.txt","r")
text = file1.read()
doc = nlp(text)
print('Names:')
false_values = ['Lender','Blvd','Borrowers','Borrower','S. Sepulveda Blvd.','Torrance','Hawthorne','P. C.','JOINTTENANTS','La Mirada','Woodward Ave','GRISELDA ACOSTA7108 MAYFLOWER A','Sioux Falls','Deborah West Roth Living Trust','Deborah West Roth']
# lets try printing on the names in from the samples text files
for entity in doc.ents:
        if(entity.label_ == "PERSON") & (entity.text not in false_values):
                print(entity.text)


file1.close()