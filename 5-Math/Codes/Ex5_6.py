#!/usr/bin/env python3

def print_result(a, b, c, d):
    print(pow(a, b) + pow(c, d))


if __name__ == '__main__':
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    print_result(a, b, c, d)
