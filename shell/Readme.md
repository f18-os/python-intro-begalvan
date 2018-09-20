CS 4375
Shell Lab

This repository contains the code for the python shell lab. The purpose is to have a shell that handles one IO redirect and one pipe.
This shell is written in Python 2.7.14.

In the repository there is a file called "shellLab.py" which is the shell.
This is an executable file that runs on Cygwin Python Version 2.7.14 
The shell's prompt is "$" and Ctrl + c is used to quit the shell.

Example:
_$ ./shellLab.py
* will run the shell

Example:
_$ Ctrl + c
* will quit the shell

This shell can handle:
* ">" redirect to
* "|" pipe

Example for redirect:
_$ echo great > output.txt
* will redirect 'great' to the file output.txt
(creates file "output.txt" and writes "echo" to it)

Example for pipe:
_$ ls | wc
* handles pipe, sends list of files to the input of wc

Please refer to COLLABORATORS file for information on collaboration and external resources.
