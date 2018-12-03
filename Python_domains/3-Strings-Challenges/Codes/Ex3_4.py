#!/usr/bin/env python3

def mutate_string(_string, _position, _character):
    temp_list = list(_string)
    temp_list[_position] = _character
    return ''.join(temp_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)