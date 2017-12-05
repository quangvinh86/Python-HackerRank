#!/usr/bin/env python3

def print_result(a, b, m):
    print(pow(a, b))
    print(pow(a, b, m))

if __name__ == '__main__':
    a, b, m = int(input()), int(input()), int(input())
    print_result(a, b, m)
