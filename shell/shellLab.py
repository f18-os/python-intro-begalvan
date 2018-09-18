#!/usr/bin/ python2

import os, sys, time, re, subprocess

def validateArgs(arguments):
        if arguments == '':
            runShell()
        
        if arguments != '':
            for dir in re.split(":", os.environ['PATH']):  # try each directory in path
                program = "%s/%s" % (dir, arguments[0])
                try:
                    os.execve(program, arguments, os.environ)  # try to exec program
                except EnvironmentError:  # ...expected
                    pass  # ...fail quietly


