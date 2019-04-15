from difflib import get_close_matches as gcm
from nltk.tokenize import word_tokenize
from nltk.corpus import words
import numpy as np


def spell_checker():
    print('Setting up dictionary......')
    # creating a set of words to form our dictionary from nltk.corpus words (~235k words)
    my_dict = set(x for x in words.words())

    # creating a set of words from an online dictionary with ~465k words
    with open('words.txt') as f:
        total = set(f.read().split())

    # combining the sets into our dictionary, creating our final dictionary of ~490k words.
    for word in total:
        my_dict.add(word.lower())

    # opening moby dick and tokenizing the words
    with open('mobydick.txt') as mb:
        orig_word_tokens = word_tokenize(mb.read())

    # here we are keeping only the tokens using the alphabet
    word_tokens = [w.lower() for w in orig_word_tokens if w.isalpha()]

    # creating our set of misspelled words
    misspelled_words = set()

    # checks if any of the tokens in moby dick are misspelled
    # and adds them to our misspelled_words set
    for w in word_tokens:
        if w.lower() not in my_dict:
            misspelled_words.add(w.lower())

    inp = int(input('Press 1 to enter your own word and use difflib.'
                    '\nPress 2 to enter your own word and use levenstein distance.'
                    '\nPress 3 to output list of misspelled words in Moby Dick.'
                    '\nPress 4 to output spellings of all misspelled words in Moby Dick.\n'))

    while True:
        if inp == 1:
            inp_word = input('enter your input word: \n')
            print(f'{inp_word}:\t{gcm(inp_word, my_dict)}')
        if inp == 2:
            inp_word = input('enter your input word: \n')
            the_count = 0
            counter = 20
            total_list = []
            print('working...', end='')
            for word in my_dict:
                now = lev(inp_word, word)
                if counter >= now:
                    the_count += 1
                    counter = now
                    total_list.append(word)
                    if the_count % 2 == 0:
                        print('.', end='')
            print()
            print(total_list[-3:])
        if inp == 3:
            print(misspelled_words)
            break
        if inp == 4:
            for w in misspelled_words:
                print(f'{w}:\t{gcm(w, my_dict)}')
            break


# took inspiration from the levenstein code online in wikipedia
def lev(mis_word, dic_word):
    if len(mis_word) < len(dic_word):
        return lev(dic_word, mis_word)

    if len(dic_word) == 0:
        return len(mis_word)

    mis_word = np.array(tuple(mis_word))
    dic_word = np.array(tuple(dic_word))

    p_row = np.arange(dic_word.size + 1)
    for s in mis_word:
        c_row = p_row + 1
        c_row[1:] = np.minimum(
            c_row[1:],
            np.add(p_row[:-1], dic_word != s))
        c_row[1:] = np.minimum(
            c_row[1:],
            c_row[0:-1] + 1)
        p_row = c_row
    return p_row[-1]


if __name__ == '__main__':
    spell_checker()
