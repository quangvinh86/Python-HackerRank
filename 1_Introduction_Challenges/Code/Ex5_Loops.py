#!/usr/bin/env python3
'''
# [Ex5_Loops](https://www.hackerrank.com/challenges/python-loops/problem)
Nhận đầu vào là một số tự nhiên N ( 1<= N <= 20). i là các giá trị thỏa mãn 0 <= i < N.
In ra màn hình các số bình phương của i. Mỗi số trên 1 dòng.
'''


def solve(input_number):
    '''
    ' params: number
    ' rtype: none
    '''
    for index in range(input_number):
        print(index ** 2)
    return None

def main():
    input_number = 5
    solve(input_number)

if __name__ == "__main__":
    main()
