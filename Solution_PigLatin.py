'''
    Pig Latin

    Write some code that translates a string (word, sentence, or paragraph) into "pig-latin" using the following rules.

    Single letters are not modified.

    Example Input:
    "HeLLo World! I can't wait to explore your VAST forests. The-End!"

    Example Output:
    "ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestfay. Hetay-Endway!"

#################################################################### orestsfay ** correction

'''

import string

letters = set(string.letters)
vowels = set(['a', 'e', 'i', 'o', 'u'])
punctuation = set(string.punctuation) - set(['-'])


def translate(word):

    if len(word) == 1:
        return word
    if len(word) >= 3 and word[-3:].lower() == 'way':
        return word
    # duplicate for varifying capital and puncs later
    original = word
    # check for vowels or consonant at the beginning of string
    # add 'way' or 'ay' accordingly
    if word[0] in letters:
        if word[0].lower() in vowels:
            word += 'way'
        else:
            word = word[1:] + word[0] + 'ay'
    # separate ascii letters from punctuation
    post_process_ascii = []
    for char in word:
        if char in punctuation:
            continue
        post_process_ascii.append(char)
    # make sure capitalization remain in the same place (from the start of the word)
    idx = 0
    for char in original:
        if char in letters:
            if char.islower():
                post_process_ascii[idx] = post_process_ascii[idx].lower()
            else:
                post_process_ascii[idx] = post_process_ascii[idx].upper()
            idx += 1
    # add punctuation back to the list in correct order
    processed_chars = []

    for i in xrange(len(original) - 1, -1, -1):
        # make sure punctuation remain in the same relative place from the end of the word
        if original[i] in punctuation:
            processed_chars.append(original[i])
        else:
            processed_chars.append(post_process_ascii.pop())
    processed_chars.extend(post_process_ascii[::-1])

    return ''.join(processed_chars[::-1])


def parse(string):
    # split by hypens, process words, then join by hypens
    words = string.split('-')
    for i in xrange(len(words)):
        words[i] = translate(words[i])
    return '-'.join(words)


def translate_to_pig_latin(s):
    i, j, res = 0, 0, []
    # two pointers
    while i < len(s):
        # what if string sarts with ' '
        # whenever encounters space, trsanslate word between pointer i and j
        if j == len(s) or s[j] == ' ':
            # check for empty string
            if i != j:
                string = s[i:j]
                res.append( parse(string) )
            # count the spaces between words (could be more than one space)
            i = j
            while j != len(s) and s[j] == ' ':
                j += 1
            res.append(' ' * (j - i))
            i = j
        else:
            j += 1
    return ''.join(res)


if __name__ == '__main__':
    # tests
    # consecutive spaces, quotation mark
    print english_to_pig_latin("HeLLo World! I can't wait to explore your VAST forests. The-End!  ")
    print english_to_pig_latin("Hi  !  ") # when there are more than one spaces in between
    print english_to_pig_latin("**")
