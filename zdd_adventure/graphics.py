#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:49:08 2022

@author: tillteb
"""
import time

# grafical funktion for printing delayed text
def delayed_print_output(pattern):
    ''' printed out a delayed version of your pattern'''
    def slower_text(pattern):
        for x in range(len(pattern)):
            print(pattern[x], end= '')
            DELAY_TIME = time.sleep(0.005)
            DELAY_TIME
    return slower_text(pattern)
