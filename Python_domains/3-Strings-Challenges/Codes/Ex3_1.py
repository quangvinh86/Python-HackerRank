#!/usr/bin/env python3

def swap_single_char(single_char):
    if single_char.islower():
        return single_char.upper()
    else:
        return single_char.lower()

def swap_case(input_string):
    return ''.join([ swap_single_char(single_char) for single_char in input_string])

if __name__ == '__main__':
    # s = input()
    s = "Www.HackerRank.com"
    result = swap_case(s)
    print(result)