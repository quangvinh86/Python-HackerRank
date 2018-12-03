#!/usr/bin/env python3
if __name__ == '__main__':
    for i in range(1, int(input()) + 1):
        print(((10**i-1)//9)**2)
    # print((''.join([str(index) for index in range(1,i+1)])).strip() + (''.join([str(jndex) for jndex in range(i-1, 0, -1)]).strip()))
