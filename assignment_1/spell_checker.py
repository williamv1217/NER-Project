import re
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import words as w

# creating a set of words to form our dictionary from nltk.corpus words (~235k words)
my_dict = set(x for x in w.words())

print(len(my_dict))
# creating a set of words from an online dictionary with ~465k words
with open('words.txt') as f:
    total = set(f.read().split())
print(len(total))
# combining the sets into our dictionary, creating our final dictionary of ~490k words.
for word in total:
    my_dict.add(word.lower())

print('final dictionary length: ', len(my_dict))



# opening moby dick and tokenizing the words
with open('mobydick.txt') as mb:
    orig_word_tokens = word_tokenize(mb.read())

# here we are keeping only the tokens using the alphabet
word_tokens = [w.lower() for w in orig_word_tokens if w.isalpha()]


# creating a set and adding the lower-case of the original word tokens
# to it in order to remove duplicates
# orig_tokens_set = set()
# for x in orig_word_tokens:
#     orig_tokens_set.add(x)


# creating our final word_tokens set, this time removing the '-' of words that end in a '-'
# we do this to remove false positives from the check against our dictionary words
# word_tokens = set()
# for i in orig_tokens_set:
#     if re.match(r'(\w+)-{1}(?!(-)|(\w+)).*', i):
#         i = i[:-1]
#         word_tokens.add(i)
#     else:
#         word_tokens.add(i)


print('len orig list: ', len(orig_word_tokens))
# print('len orig set: ', len(orig_tokens_set))
print('len new set: ', len(word_tokens))


# creating our set of misspelled words
misspelled_words = set()

# checks if any of the tokens in moby dick are misspelled
# and adds them to our misspelled_words set
for w in word_tokens:
    if w.lower() not in my_dict:
        misspelled_words.add(w.lower())
# mw = set()
# for w in orig_word_tokens:
#     if w not in my_dict:
#         mw.add(w)

print(len(misspelled_words))
print(misspelled_words)
# print(len(mw))
# print(mw)
# TODO: create the actual spell checker

