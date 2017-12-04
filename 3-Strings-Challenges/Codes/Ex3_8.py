#!/usr/bin/env python3
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    # S = input()
    # in = int(input())
    S = "bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd"
    n = 9
    print(wrap(S, n))
