#!/usr/bin/env python3

def validate_string(input_string):
    # alphanumeric
    print(any([sg_char.isalnum() for sg_char in input_string]))
    # alphabetical
    print(any([sg_char.isalpha() for sg_char in input_string]))
    # Digits
    print(any([sg_char.isdigit() for sg_char in input_string]))
    # lowercase
    print(any([sg_char.islower() for sg_char in input_string]))
    #uppcase
    print(any([sg_char.isupper() for sg_char in input_string]))


if __name__ == '__main__':
    # s = input()
    s = "1q2w3e4r@A"
    validate_string(s)
