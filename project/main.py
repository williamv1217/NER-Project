import spacy
from spacy import displacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')


with open('mobydick_test.txt', 'r') as f:
    moby_dick_text = f.read()


doc = nlp(moby_dick_text)
print(len(doc.ents))


labels = [x.label_ for x in doc.ents]
q = Counter(labels)
for x in q.most_common():
    print(x)

sentences = [x for x in doc.sents]
print(sentences[90])

displacy.render(nlp(str(sentences[90])))