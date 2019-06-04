import glob
import os
from collections import defaultdict

brownPath = '/Users/William/nltk_data/corpora/brown'

files = glob.glob(brownPath + "/c[a-z][0-9][0-9]")
numFiles = 0
numSentences = 0

categories = open(brownPath + "/cats.txt", "r")
cats = defaultdict(str)
for line in categories:
    (f, cat) = line.strip().split()
    cats[f] = cat

numFilesCat = defaultdict(int)
numSentencesCat = defaultdict(int)
numWordsCat = defaultdict(int)

wFreq = defaultdict(int)
pFreq = defaultdict(int)

wpFreq = defaultdict(int)

wwFreq = defaultdict(int)
ppFreq = defaultdict(int)

for file in files:
    f = open(file, 'r')
    numFiles += 1
    (path, filename) = os.path.split(file)
    cat = cats[filename]
    numFilesCat[cat] += 1

    for line in f:
        words = list()
        psos = list()

        if line.strip():
            numSentences += 1
            numSentencesCat[cat] += 1
            data = line.strip().split()
            data = [x.split("/") for x in data]
            (words, psos) = zip(*data)
            numWordsCat[cat] += len(words)

        if len(words) != len(psos):
            print(line)
            print("ERROR: corpus splitting: " + str(words) + str(psos))
            exit(0)

        if len(words):  # ASSERT len words == len psos
            for i in range(0, len(words)):
                wFreq[words[i]] += 1
                pFreq[psos[i]] += 1

                wpFreq[(words[i], psos[i])] += 1

                if i == 0:
                    wwFreq[("^^", words[i])] += 1
                    ppFreq[("^^", psos[i])] += 1

                if i < len(words) - 1:
                    wwFreq[(words[i], words[i + 1])] += 1
                    ppFreq[(psos[i], psos[i + 1])] += 1
                else:
                    wwFreq[(words[i], "$$")] += 1
                    ppFreq[(psos[i], "$$")] += 1

    f.close()

print("Brown Path: " + brownPath)
print("Num Files: " + str(numFiles))
print("Num Sentences: " + str(numSentences))

print(
    "Files are organized a sentence per line, noting some lines are blank, with words and parts of speech separated by a slash.")
print("The filenames correspond to categories, defined in cats.txt file.")

# category stats
f1 = open("cFreq", "w")
for cat in numSentencesCat:
    f1.write(
        cat + "\t" + str(numFilesCat[cat]) + "\t" + str(numSentencesCat[cat]) + "\t" + str(numWordsCat[cat]) + "\n")
print("cFreq is written to disk")


# singletons: word and pos
f1 = open("wFreq", "w")
for word in wFreq:
    f1.write(word + "\t" + str(wFreq[word]) + "\n")
print("wFreq is written to disk")


f1 = open("pFreq", "w")
for pos in pFreq:
    f1.write(pos + "\t" + str(pFreq[pos]) + "\n")
print("pFreq is written to disk")


# bigrams: words and parts of speech
f1 = open("wwFreq", "w")
for (word1, word2) in wwFreq:
    f1.write(word1 + "\t" + word2 + "\t" + str(wwFreq[(word1, word2)]) + "\n")
print("wwFreq is written to disk")


f1 = open("ppFreq", "w")
for (pos1, pos2) in ppFreq:
    f1.write(pos1 + "\t" + pos2 + "\t" + str(ppFreq[(pos1, pos2)]) + "\n")
print("ppFreq is written to disk")


# parts of speech: word-POS frequencies
f1 = open("wpFreq", "w")
for (word, pos) in wpFreq:
    f1.write(word + "\t" + pos + "\t" + str(wpFreq[(word, pos)]) + "\n")
print("wpFreq is written to disk")
