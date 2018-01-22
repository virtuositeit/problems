'''
    Essay Monkey
    Given a set of txt files generate an essay.

    The function should take the number of paragraphs to generate.
    The function should take the number of sentences per peragraph to generate.
    Each sentence should be of any reasonable length but each should not be the same length.

    Input
    See EssayMonkeyVerbs.txt
    See EssayMonkeyNouns.txt
    See EssayMonkeyAdjectives.txt

    Examples:
    'dogs swim' (n v)
    'i am happy' (n v adj)
    'is he tall?' (v n adj)
    'i eat cool food' (n v adj n)
    'elegant pies gather unadvised coal' (adj n v adj n)
    'big 256 byte packet data buffer' (adj adj n n n n)

    (sentences can start and end with a verb, noun, or adjective)

'''

from __future__ import print_function
import random
import sys


# initialize a container for words from input files
words = { 'v': [],
          'n': [],
          'adj': []
        }
# syntax denotes the type of words that'd be grammatically correct to follow the current word
# e.g. play (v.) + ball (n.)
syntax = { 'v': ['n', 'adj'],
           'n': ['v', 'n', 'adj'],
           'adj': ['n', 'adj']
         }

# Situation 1: Input word files are huge. (see method 1)
#              -> Use f.read() to read by char, then return each word by yield

# Situation 2: Input word files aren't huge, or the program is run very often
#              -> Read all the words for once upfront and store them in a list

def gen_sentence(sentence_len):
    sentence, length = [], 0
    next_word_type = random.choice(['v', 'n', 'adj'])
    for i in xrange(sentence_len):
        sentence.append( random.choice( words[next_word_type] ) )
        next_word_type = random.choice( syntax[next_word_type] )
    sentence[-1] += '.'
    return ' '.join(sentence)


# paragraph_num: number of paragraphs to generate
# sentence_num: number of sentences per paragraph
def gen_paragraph(paragraph_num, sentence_num):
    # starts with min sentence length
    sentence_len = 2

    for i in xrange(paragraph_num):
        for j in xrange(sentence_num):
            sentence = gen_sentence(sentence_len)
            print(sentence, end=' ')
            sentence_len += 1
        print('\n')


def read_file(filename):
    if 'Verb' in filename:
        word_type = 'v'
    elif 'Noun' in filename:
        word_type = 'n'
    elif 'Adjective' in filename:
        word_type = 'adj'
    else:
        sys.exit('Cannot find verb, noun, or adjective word files')

    with open(filename, 'r') as f:
        string = f.read()
        string = string.strip(' ,\n')
        all_words = string.split(',')
        for i, word in enumerate(all_words):
            all_words[i] = word.rstrip(' \n\t')
        words[word_type] = all_words

    # Exceptions: 'used (to)', 'was/were'


def main():
    files = ['./EssayMonkeyVerbs.txt', './EssayMonkeyNouns.txt', './EssayMonkeyAdjectives.txt']
    # Load and process words from files
    try:
        for filename in files:
            read_file(filename)
    except:
        sys.exit('Please make sure the verbs, nouns, adjectives word files are in the same directory as the .py file!')

    # Get user input
    while True:
        try:
            print('Hi there! Essay Monkey here. Let\'s write an essay today!')
            paragraph_num = input('How many paragraphs would you like to generate? ')
        except:
            print('Please provide the number of paragraphs to generate!')
            continue
        else:
            break

    while True:
        try:
            sentence_num = input('How many sentences per paragraph would you like to generate? ')
            print('')
        except:
            print('Please provide an integer as the number of sentences to generate!')
            continue
        else:
            break

    gen_paragraph(paragraph_num, sentence_num)


if __name__ == '__main__':
    main()
