import time
import sys
from os import system, name
import os
import datetime

# grafical funktion for printing delayed text
def delayed_print_output(pattern):
    ''' printed out a delayed version of your pattern'''
    def slower_text(pattern):
        for x in range(len(pattern)):
            print(pattern[x], end= '')
            sys.stdout.flush()
            DELAY_TIME = time.sleep(0.5)
            DELAY_TIME
    return slower_text(pattern)

# countdown 
def countdown(time_sec):
    
    while time_sec >= 0:
        sys.stdout.write("\r%s" % str(datetime.timedelta(seconds=time_sec)))
        sys.stdout.flush()
        time_sec -= 1
        time.sleep(1)

def clear_cmd():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def ascii_output(picture):
    root = os.getcwd()
    filename = os.path.join(root, "ASCII_art", picture)
    ascii_data = open(filename,"r")
    content = ascii_data.read()
    ascii_data.close()
    print(content)