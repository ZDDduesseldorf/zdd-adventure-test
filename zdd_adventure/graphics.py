#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:49:08 2022

@author: tillteb
"""
import time
import sys
import datetime

# grafical funktion for printing delayed text
def delayed_print_output(pattern):
    ''' printed out a delayed version of your pattern'''
    def slower_text(pattern):
        for x in pattern:
            print(x, end= '')
            sys.stdout.flush()
            DELAY_TIME = time.sleep(0.005)
            DELAY_TIME
    return slower_text(pattern)

# countdown 
def countdown(time_sec):
    
    while time_sec >= 0:
        sys.stdout.write("\r%s" % str(datetime.timedelta(seconds=time_sec)))
        sys.stdout.flush()
        time_sec -= 1
        time.sleep(1)
