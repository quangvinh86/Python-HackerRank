#!/usr/bin/env python3

def find_second_largest(integer_list):
    return sorted(list(set(integer_list)))[-2]


if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())
    integer_list = map(int, "1 -4 0 -2 -4".split())
    print(find_second_largest(integer_list))
