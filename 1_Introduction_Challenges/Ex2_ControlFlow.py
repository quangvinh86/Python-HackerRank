#!/usr/bin/env python3
'''
**Ex2_ControlFlow**
Nhận đầu vào là một số nguyên n: 1 <= n <= 100
Viết chương trình in ra màn hình:
- Nếu n là số lẻ, in ra Weird
- Nếu n là số chẵn và nằm trong khoảng 2 -5, in ra Not Weird
- Nếu n là số chẵn và nằm trong khoảng 6 - 20, in ra Weird
- Nếu n là số chẵn và lớn hơn 20, in ra Not Weird
'''


def solve(input_data):
    '''
    ' params: number
    ' rtype: string
    '''
    if input_data % 2 or 6 <= input_data <= 20:
        return "Weird"
    else:
        return "Not Weird"


def main():
    input_number = 21
    print(solve(input_number))


if __name__ == "__main__":
    main()
