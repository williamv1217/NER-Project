from nltk.corpus import brown
from nltk.util import ngrams

from collections import Counter
print('s')
unigrams = ngrams(brown.words(), 1)
unigram_freq = Counter(unigrams)
print('hi')
print(unigrams)
import itertools



# bigrams = ngrams(brown.words(), 2)
# bigram_freq = Counter(bigrams)
#
# trigrams = ngrams(brown.words(), 3)
# trigram_freq = Counter(trigrams)

# print('total distinct unigrams: ', len(unigram_freq))
# print('total distinct bigrams: ', len(bigram_freq))
# print('total distinct trigrams: ', len(trigram_freq))
#
# # print(bigram_freq.most_common(5))
# print('the President: ', bigram_freq.get(('the', 'President')))
# print('the Russian: ', bigram_freq.get(('the', 'Russian')))
# print('boiled haddock: ', bigram_freq.get(('boiled', 'haddock')))

# print(trigram_freq.most_common())

# ds1 = set()
# for x in brown.words():
#     tf = trigram_freq.get(('ran', 'the', x))
#     if tf is not None:
#         ds1.add((x, tf))
#         # print(f"('ran', 'the', {x}) --- {tf}")
# print(ds1)
# print(sorted(ds1))

#
# x = 'abcaaabcdec'
# c = Counter(x)
# print(c)
# print(len(c))
# print(sum(c.values()))

