#!/usr/bin/env python3
import math

if __name__ == '__main__':
    AB, BC = input("AB"), input("BC")
    print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')

