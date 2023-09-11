#!/usr/bin/python3
def no_c(my_string):
    r = 0
    new_string = my_string[:]
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_string = new_string[:(i - r)] + my_string[i + 1:]
            r += 1
    return new_string
