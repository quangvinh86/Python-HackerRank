#!/usr/bin/env python3

def count_substring(string, sub_string):
    # Fastest
    return sum([1 for i in range(0, len(string)) if string[i:i+len(sub_string)] == sub_string])
    # explain: List comprehesion like codes
    # summ = 0
    # for (i in range(len(string)))
    # if (string[i:i+len(sub_string)] == sub_string))
    #     summ += 1


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = ("In this challenge, the user enters a string and a substring."
              "You have to print the number of times that the substring "
              "occurs in the given string")
    sub_string = "string"
    count = count_substring(string, sub_string)
    print(count)
