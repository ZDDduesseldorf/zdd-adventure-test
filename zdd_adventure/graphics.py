import time
import sys
from os import system, name
import os
import datetime

# grafical funktion for printing delayed text
def delayed_print_output(pattern, print_speed=0.05): #print_speed ist time.sleep value
    ''' printed out a delayed version of your pattern'''
    def slower_text(pattern):
        for x in range(len(pattern)):
            print(pattern[x], end= '')
            sys.stdout.flush()
            DELAY_TIME = time.sleep(print_speed)
            DELAY_TIME
    return slower_text(pattern)

# countdown 
def countdown(time_sec):
    
    while time_sec >= 0:
        sys.stdout.write("\r%s" % str(datetime.timedelta(seconds=time_sec)))
        sys.stdout.flush()
        time_sec -= 1
        time.sleep(1)

#  clear terminal/ CMD
def clear_cmd():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# read/ print .txt file
# > picture = filename.txt 
# > delay = print with delayed_print_output method 
# > print_speed = time.sleep value
def ascii_output(picture, delay=False, print_speed=0.001):
    root = os.getcwd()
    filename = os.path.join(root, "ASCII_art", picture)
    ascii_data = open(filename, "r", encoding="utf-8")
    image_str = ascii_data.read()
    
    if delay == True:
        delayed_print_output(image_str, print_speed)
        
    else:
        print(image_str)
        
    ascii_data.close()