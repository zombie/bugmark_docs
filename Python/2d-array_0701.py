#!/usr/bin/env python3

# Question:
# Write a Python program which takes 2 digits, X,Y as input and generates a
# 2-dimensional array with these dimensions. The element value in the i-th row and j-th column
# of the array should be i*j.
#
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
# Hints:
# Note: In case of input data being supplied to the question, it should be
# assumed to be a console input in a comma-separated form.
#
#
# Solution:

import os, sys

def make_row(i, y):
    return [i*j for j in range(y)]

def make_2d_array(x,y):
    return [make_row(i, y) for i in range(x)]

if __name__ == '__main__':
    if os.isatty(0): # Prompt if run from an interactive shell
        prompt = 'Enter x, y: '
    else:
        prompt = ''
    try:
        (x,y) = [int(i) for i in input(prompt).split(',')]
    except ValueError:
        sys.exit("Bad input format. Enter x,y") 
    print(make_2d_array(x, y))
