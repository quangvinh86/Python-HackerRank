#!/usr/bin/env python3

def create_tuple(integer_list):
    my_tuple = tuple(integer_list)
    print(hash(my_tuple))

if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    create_tuple(integer_list)
