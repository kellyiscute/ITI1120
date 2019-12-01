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


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    result = {}
    lines = fp.read().splitlines()
    i: str
    w_count = {}
    for i in lines:
        words = i.lower().split()
        remove_punctuations(words)
        remove_hyphen_apostrophes(words)
        words = remove_short_words(words)
        for j in words:
            w_count[j] = 1
    return w_count


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    pass


##############################
# main
##############################
file = open_file()
d = read_file(file)
query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
