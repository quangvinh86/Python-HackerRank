#!/usr/bin/env python3

def print_formatted(input_number):
    width = len(bin(input_number)[2:])
    for i in range(1, input_number + 1):
        print (str(i).rjust(width,' '),str(oct(i)[2:]).rjust(width,' '),str(hex(i)[2:].upper()).rjust(width,' '),str(bin(i)[2:]).rjust(width,' '),sep=' ')


if __name__ == '__main__':
    # n = input()
    n = 17
    print_formatted(n)
