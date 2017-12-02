#!/usr/bin/env python3
'''
# [Ex6_Function](https://www.hackerrank.com/challenges/write-a-function/problem)
Chúng ta thường có thêm một ngày 29/2 sau mỗi 4 năm. Ngày này gọi là ngày nhuận.
Theo lịch Gregorian điều kiện để 1 năm có ngày nhuận như sau:
- Một năm chia hết cho 4 sẽ là năm nhuận trừ trường hợp ngoại lệ:
    - Nếu năm đó chia hết cho 100 nhưng không chia hết cho 400 thì không phải năm nhuận
    - Nếu năm đó chia hết cho 100 và chia hết cho 400 thì là năm nhuận
Ví dụ: 
Năm 1800, 1900, 2100, 2200, 2300 và 2500 không phải là năm nhuận vì chia hết cho 4 nhưng không chia hết cho 400
Năm 2400, 2000 là năm nhuận vì chia hết cho 400.

Viết một function nhận đầu vào là một năm, kiểm tra xem năm đó là năm nhuận hay không.

'''

def is_leap(year):
    leap = False
    if not year % 400:
        leap = True
    elif (not year % 4) and (year % 100):
        leap = True
    return leap

def main():
    print(is_leap(2000))
    print(is_leap(1800))
    print(is_leap(2100))
    print(is_leap(1996))

if __name__ == "__main__":
    main()
