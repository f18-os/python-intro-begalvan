CS 4375
Blanca Galvan
Shell Lab

This repository contains the code for the python shell lab. The
purpose is to have a shell that handles one IO redirect and one pipe.
This shell is written in Python 2.7.14.

In the repository there is a file called "shellLab.py" which is the shell.
This is an executable file that runs on Cygwin Python Version 2.7.14 
The shell's prompt is "$", "q" is used to quit the shell.
This shell can handle:
* ">" redirect to
* "ls|wc" pipe

Example:
'_$ ./shellLab.py`
* will run the shell
'_$ echo `
* excluding white space and punctuation
* is case-insensitive
* print out to the output file (overwriting if it exists) the list of
  words sorted in descending order with their respective totals
  separated by a space, one word per line

To test your program we provide wordCountTest.py and two key
files. This test program takes your output file and notes any
differences with the key file. An example use is:

`$ python wordCountTest.py declaration.txt myOutput.txt declarationKey.txt`

The re regular expression library and python dictionaries should be
used in your program. 

Note that there are two major dialects of Python.  Python 3.0 is
incompatible with 2.7.   As a result, Python 2.7 remains popular.  All
of our examples are in 2.7.  We (mildly) encourage students to use 2.7
for their assignments. 
