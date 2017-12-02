#!/usr/bin/env python3
'''

'''


def squared(input_data):
    '''Tính bình phương của số đầu vào
    ' params: number
    ' rtype: number
    '''
    result = None
    result = input_data ** 2
    return result

def squared_root(input_data):
    '''Tính căn bậc 2 của số đầu vào
    ' params: number
    ' rtype: number
    '''
    result = math.sqrt(input_data)
    return result

def main():
    input_number = 16
    print("squared: ", squared(input_number))
    print("squared root: ", squared_root(input_number))


if __name__ == "__main__":
    main()
