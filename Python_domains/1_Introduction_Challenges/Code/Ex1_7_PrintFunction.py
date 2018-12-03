#!/usr/bin/env python3
'''
# [Ex7_Print_Function](https://www.hackerrank.com/challenges/python-print/problem)
Nhận đầu vào là một số nguyên.
In ra màn hình các số nguyên từ 1 đến N trên cùng một dòng.
Ví dụ: N = 3 --> in ra màn hình 123

'''

def print_number(input_number):
    print(''.join([str(x) for x in range(1, input_number + 1)]))

def main():
    input_number = 10
    print_number(input_number)


if __name__ == "__main__":
    main()
