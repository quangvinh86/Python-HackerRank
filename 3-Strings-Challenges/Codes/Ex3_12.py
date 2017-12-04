#!/usr/bin/env python3
def capitalize(string):
    return ' '.join([sub.capitalize() for sub in string.split(" ")])


if __name__ == '__main__':
    # string = input()
    string = "1 w 2 r 3g"
    capitalized_string = capitalize(string)
    print(capitalized_string)
