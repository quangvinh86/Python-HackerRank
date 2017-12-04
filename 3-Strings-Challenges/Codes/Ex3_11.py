#!/usr/bin/env python3
import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    my_list = ['-'.join((alpha[i:n][::-1] + alpha[i:n][1:]).center(2*size-1,"-")) for i in range(n)]
    print('\n'.join(my_list[::-1] + my_list[1:]))


if __name__ == '__main__':
    # n = input()
    n = 5
    print_rangoli(n)
