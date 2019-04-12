import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words
import re
import time


x = ['hello', 'hi-', 'bye-', 'hi-q23', 'hi--nono', 'h---no3']
x2 = []
tok = RegexpTokenizer(r'\w+')

print(tok.tokenize(x))




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
