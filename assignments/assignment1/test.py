import nltk
from nltk.tag import pos_tag, map_tag
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.corpus import words
import re
import time

# NLTK Universal Tagset:

# VERB - verbs (all tenses and modes)
# NOUN - nouns (common and proper)
# PRON - pronouns
# ADJ - adjectives
# ADV - adverbs
# ADP - adpositions (prepositions and postpositions)
# CONJ - conjunctions
# DET - determiners
# NUM - cardinal numbers
# PRT - particles or other function words
# X - other: foreign words, typos, abbreviations
# . - punctuation

text = word_tokenize('Book the dinner flight.')
print(pos_tag(text, tagset='universal'))

text2 = word_tokenize('I prefer flights to Houston.')
print(pos_tag(text2, tagset='universal'))



# print(nltk.help.upenn_tagset('ADP'))
# print(nltk.help.upenn_tagset('IN'))
# for i in x:
#     if re.match(r'(\w+)-{1}(?!(-)|(\w+)).*', i):
#         # print(i)
#         i = i[:-1]
#         x2.append(i)
#     else:
#         x2.append(i)
#
# print(x2)


# match = []
# filename = "mobydick.txt"
# filename2 = 'tokens.txt'
# with open(filename) as f:
#     for line in f:
#         x = re.search(r'\bant\w*\b', line)
#         if x is not None:
#             match.append(x)
#
# print(len(match))
#
# for x in match:
#     print(x)
#
#
# biggest = 0
# biggest_word = ""
#
# with open(filename2) as f:
#     for line in f:
#         if len(line) > biggest:
#             biggest = len(line)
#             biggest_word = line
#
#
# print(biggest, ' ', biggest_word)
