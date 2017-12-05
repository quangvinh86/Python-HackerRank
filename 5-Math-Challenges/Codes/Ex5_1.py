#!/usr/bin/env python3
import cmath

def convert_polar_coordinates(complex_number):
    print("{:.3f}\n{:.3f}".format(*cmath.polar(complex_number)))

if __name__ == '__main__':
    complex_number = complex(input())
    convert_polar_coordinates(complex_number)
