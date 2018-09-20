#!/usr/bin/env python2

import os, sys, time, re, subprocess

def validateArgs(arguments,allCmd):
        if arguments == '':
            runShell()
        
        if arguments != '':
            for dir in re.split(":", os.environ['PATH']):  # try each directory in path
                program = "%s/%s" % (dir, arguments[0])
                try:
                    os.execve(program, arguments, os.environ)  # try to exec program
                except EnvironmentError:  # ...expected
                    pass  # ...fail quietly
def redirect(allCmd): #redirect to
      redirect = allCmd.split(">")
      needsToRedirect = len(redirect) > 1
      executeCmd(redirect[0], needsToRedirect, redirect[1].strip() if needsToRedirect else "")

def getArgs(allCmd):  #get arguments for pipe 
        pipe = allCmd.split("|")
        if len(pipe) == 1:
            return filter(None, allCmd.split(" "))

        else:
            cmd = pipe[1].strip()
            process = subprocess.Popen(allCmd, stdout=subprocess.PIPE, shell=True)
            response = process.communicate()[0]
            print(response)
            return ""

def executeCmd(allCmd, redirect=False, redirectSource=""):
    pid = os.getpid()
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:  # child
        if redirect:
            os.close(1)  # redirect child's stdout
            sys.stdout = open(redirectSource, "w") #write to and create file

        arguments = getArgs(allCmd)
        validateArgs(arguments, allCmd)

        os.write(2, ("Child: Error: Could not exec %s\n" % arguments[0]).encode())
        sys.exit(1)  # terminate with errorq

    else:  # parent (forked ok)
        childPidCode = os.wait()

def runShell():
    try:
        while True:
            allCmd = raw_input(os.environ['PS1'])
            redirect(allCmd)
    except KeyboardInterrupt: #Ctrl + c quits shell
            sys.exit()
            
runShell()
