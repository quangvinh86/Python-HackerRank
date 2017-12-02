#!/usr/bin/env python3
'''
[**Ex4_Division**](https://www.hackerrank.com/challenges/python-division/problem)

Nhận đầu vào là 2 số tự nhiên và in ra hai dòng:
- Dòng đầu là số nguyên của phép chia a//b
- Dòng thứ hai là số thực của phép chia a/b

Ghi chú: không làm tròn hoặc format lại số.

'''


def solve(first_input, second_input):
    '''
    ' params: two number
    ' rtype: none
    '''
    print(first_input // second_input)
    print(first_input / second_input)
    return None

def main():
    first_input = 4
    second_input = 3
    solve(first_input, second_input)


if __name__ == "__main__":
    main()
