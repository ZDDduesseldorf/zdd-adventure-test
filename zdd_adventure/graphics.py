import time
import sys
from os import system, name
import os
import datetime

# grafical funktion for printing delayed text
# print_speed = time.sleep value
def slow_print(pattern, print_speed=0.05):
	for i in pattern + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(print_speed)

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
    filename = os.path.join(root + "//ASCII_art//" + picture)
    ascii_data = open(filename, "r", encoding="utf-8")
    image_str = ascii_data.read()

    if delay == True:
        slow_print(image_str, print_speed)

    else:
        print(image_str)

    ascii_data.close()



'''  ANIMATIONS  '''

def slow_list_print(output_list, delay=1):
    """and this function will just print the single words of
       your list delayed."""

    for i in output_list:
       print(i)
       time.sleep(delay)

def percent(delay=0.02):
    """prints till 100%"""

    def status(percent):
        sys.stdout.write(f"\r{percent}%")
        sys.stdout.flush()

    for i in range(0,101):
        time.sleep(delay)
        status(i)

# going lower than 0.2 in timing can lead to skipped frames
# animate a singular line; can be used without time with standard time of 0.2 per frame
def animate_one_line(animations, timing = []):
    for i in range(0,len(animations)):
        sys.stdout.write(f"\r{animations[i]}")
        sys.stdout.flush()
        if len(timing) != 0:
            time.sleep(timing[i])
        else:
            time.sleep(0.2)

# skip a certain amount of number; by default 40 (whole input terminal)
def skip_frames(n=40):
    print(n*"\n")

# animates multiple lines; can be used without time with standard time of 0.2 per frame
def animate_multiple_lines(animation, timing=[], repetitions = 10):
    for _ in range(repetitions):
        for i in range(0,len(animation)):
            skip_frames()
            sys.stdout.write(animation[i])
            if len(timing) != 0:
                time.sleep(timing[i])
            else:
                time.sleep(0.2)
            sys.stdout.flush()

# If examples are needed:

# animationsUwU = ["OwO", "owo", "-w-", "owo"]
# timeUwU = [1, 0.1, 0.2, 0.1]
# while True:
#     animate_one_line(animationsUwU, timeUwU)

# animationsDance = [" O \n-\\-\n /\\ ", " O \n-/-\n/\\ "]
# timeDance = [0.3, 0.3]
# animate_multiple_lines(animationsDance, timeDance) #<-- klappt auch ohne time
