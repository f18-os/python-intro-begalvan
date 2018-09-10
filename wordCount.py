#! /usr/bin/env python3

import sys  # command line arguments
import re  # regular expression tools
import os


# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

input = sys.argv[1]
output = sys.argv[2]

# use findall() -> to find all matches and return key string
def findall(key, text_string):
    find_all = re.findall(r'\b' + key + '\\b', text_string)
    for word in find_all:
        count = relat.get(key, 0)
        relat[word] = count + 1
    return relat.keys()

# to end program
def end():
    print("Passed")
    file.close()
    exit()

# to clean text -> take out numbers
def clean_numbers(doc):
    no_numbers = ''
    i = 0
    for word in doc:
        no_numbers += re.sub('[0-9]', '', word)

    words = no_numbers.split()
    return words


def list_appended(words, text_string):
    list_append = []
    index = 0
    for i in words:
        list_append.append(findall(words[index], text_string))
        index += 1
    return list_append

key = open('speechKey.txt')
read_key = key.read()
words = clean_numbers(read_key)
relat = {}
essay = open(input, 'r')
text_string = essay.read().lower()
dict = list_appended(words, text_string)

position = 0
os.remove(output)
for words in dict[1]:
    file = open(output, 'a')
    file.write(words + " " + str(relat[words]) + "\n")
    position += 1
    if position == len(dict[1]):
        end()