import string
import typing


def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    file = None
    while file is None:
        filename = input('Enter the name of the file: ')
        try:
            f = open(filename, 'r')
            file = f
        except OSError:
            print('There is no file with that name. Try again.')
            continue

    return file


def remove_punctuations(l: typing.List[str]):
    for i in range(len(l)):
        l[i] = l[i].replace(',', '')
        l[i] = l[i].replace('.', '')
        l[i] = l[i].replace('!', '')


def remove_hyphen_apostrophes(l: typing.List[str]):
    for i in range(len(l)):
        l[i] = l[i].replace('-', '')
        l[i] = l[i].replace('\'', '')


def remove_short_words(l: typing.List[str]):
    result = []
    for i in l:
        if len(i) > 1:
            result.append(i)
    return result


def remove_non_alphabetic(l: typing.List[str]):
    result = []
    for i in l:
        if i.isalpha():
            result.append(i)
    return result


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    result: typing.Dict[str, set] = {}
    lines = fp.read().splitlines()
    fp.close()
    for i in range(len(lines)):
        words = lines[i].lower().split()
        remove_punctuations(words)
        remove_hyphen_apostrophes(words)
        words = remove_non_alphabetic(words)
        words = remove_short_words(words)
        for j in words:
            if j not in result:
                result[j] = set()
            if i + 1 not in result[j]:
                result[j].add(i + 1)
    return result


def find_coexistance(D: dict, query: str):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    l = query.split()
    remove_hyphen_apostrophes(l)
    found_words: typing.List[set] = []
    for i in l:
        if i in D:
            found_words.append(D[i])
    result = found_words[0]
    for i in found_words:
        result = i.intersection(result)
    return result


##############################
# main
##############################
file = open_file()
d = read_file(file)
query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
# YOUR CODE GOES HERE
while query != 'q':
    words = query.split()
    remove_hyphen_apostrophes(words)
    flg_word_not_exist = False
    for w in words:
        if w not in d:
            print(f'Word \'{w}\' not in the file.')
            flg_word_not_exist = True
            break
    if flg_word_not_exist:
        query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
        continue
    print('The one or more words you entered coexisted in the following lines of the file:')
    print(find_coexistance(d, query))
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
