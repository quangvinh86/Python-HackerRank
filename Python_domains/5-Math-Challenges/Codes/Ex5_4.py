#!/usr/bin/env python3

def print_result(a, b):
    print(a // b)
    print(a % b)
    print(divmod(a, b))

if __name__ == '__main__':
    a, b = int(input()), int(input()) 
    print_result(a, b)
