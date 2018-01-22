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
words = { 'v': None,
          'n': None,
          'adj': None
        }
# syntax denotes the type of words that'd be grammatically correct to follow the current word
# e.g. play (v.) + ball (n.)
syntax = { 'v': ['n', 'adj'],
           'n': ['v', 'n', 'adj'],
           'adj': ['n', 'adj']
         }

# Situation 1: Input word files are huge.
#              -> Use f.read() to read by char, then return each word by yield

# Situation 2: Input word files aren't huge, or the program is run very often (see method 2)
#              -> Read all the words for once upfront and store them in a list

def gen_word(filename):
    while True:
        with open(filename, 'r') as f:
            char_list = []
            while True:
                # read the file a char at a time
                # join chars as a word when a ',' or '/', or EOF is encountered
                char = f.read(1)
                if not char or char == ',' or char == '/':
                    word = ''.join(char_list)
                    word = word.strip(' \n\t')
                    yield word
                    # when EOF reached, break out of the loop, and reopen the file
                    if not char:
                        break
                    else:
                        char_list = []
                elif char == '(' or char == ')' or char == '\n' or char == '\t':
                    continue
                else:
                    char_list.append(char)


def gen_sentence(sentence_len):
    sentence, length = [], 0
    next_word_type = random.choice(['v', 'n', 'adj'])
    for i in xrange(sentence_len):
        sentence.append( next(words[next_word_type]) )
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


def main():
    files = ['./EssayMonkeyVerbs.txt', './EssayMonkeyNouns.txt', './EssayMonkeyAdjectives.txt']
    # Load and process words from files
    try:
        words['v'] = gen_word('./EssayMonkeyVerbs.txt')
        words['n'] = gen_word('./EssayMonkeyNouns.txt')
        words['adj'] = gen_word('./EssayMonkeyAdjectives.txt')
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
