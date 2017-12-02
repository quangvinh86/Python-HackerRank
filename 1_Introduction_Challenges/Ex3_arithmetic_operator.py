#!/usr/bin/env python3
'''
**[Ex3_Arithmetic_Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem)**

Nhận đầu vào là 2 số tự nhiên và in ra 3 dòng với điều kiện:
- Dòng thứ nhất chứa tổng của 2 số.
- Dòng thứ hai chứa hiệu của 2 số (số thứ 1 trừ số thứ 2)
- Dòng thứ ba chứa tích của hai số.
'''


def solve(first_input, second_input):
    '''
    ' params: two number
    ' rtype: none
    '''
    print(first_input + second_input)
    print(first_input - second_input)
    print(first_input * second_input)
    return None

def main():
    first_input = 3
    second_input = 2
    solve(first_input, second_input)


if __name__ == "__main__":
    main()
