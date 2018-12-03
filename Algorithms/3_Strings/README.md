
### Super Reduced String
https://www.hackerrank.com/challenges/reduced-string/problem



```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(origin_str):
    if not origin_str:
        return "Empty String"
    result = []
    for char in origin_str:
        if result and result[-1] == char:
            result.pop()
        else:
            result.append(char)
    if result:
        return "".join(result)
    else:
        return "Empty String"
            

if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)
    print(result)

#     fptr.write(result + '\n')

#     fptr.close()

```

    baab
    Empty String


### Strong Password
https://www.hackerrank.com/challenges/strong-password/problem



```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimum_number(n, password):
    digit, lower, upper, special = 1, 1, 1, 1
    special_characters = "!@#$%^&*()-+"
    for char in password:
        if digit and char.isdigit():
            digit = 0
        if lower and char.islower():
            lower = 0
        if upper and char.isupper():
            upper = 0
        if special and char in special_characters:
            special = 0
    return max(digit + lower + upper + special, 6 - n)
        
if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimum_number(n, password)

#     fptr.write(str(answer) + '\n')

#     fptr.close()
    print(answer)

```

    4
    4700
    3


### Two Characters
https://www.hackerrank.com/challenges/two-characters/problem



```python
#!/bin/python3

import math
import os
import random
import re
import sys

def check_valid_string(remain_string):
    last_char = remain_string[0]
    for char in remain_string[1:]:
        if last_char == char:
            return False
        else:
            last_char = char
    return True
        
def get_remain_string(chars, value, original_str):
    remove_set = chars - value
    for remove_str in list(remove_set):
        original_str = original_str.replace(remove_str, "")
    return original_str

def find_max_lenght(chars, original_str):
    max_lenght = 0
    list_chars = list(chars)
    for index, first in enumerate(list_chars[:len(list_chars)-1]):
        for second in list_chars[index + 1:]:
            value = set(first + second)
            remain_string = get_remain_string(chars, value, original_str)
            if check_valid_string(remain_string):
                max_lenght = max(max_lenght, len(remain_string))            
    return max_lenght


# Complete the alternate function below.
def alternate(original_str):
    chars = set(original_str)
    if len(chars) < 2:
        return 0
    if len(chars) < 3:
        return len(original_str)
    else: 
        return find_max_lenght(chars, original_str)


if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())
    s = input()

    result = alternate(s)
    print(result)

#     fptr.write(str(result) + '\n')

#     fptr.close()

```

    28
    asdcbsdcagfsdbgdfanfghbsfdab
    8


### Caesar Cipher
https://www.hackerrank.com/challenges/caesar-cipher-1/problem



```python
122 - 97
```




    25




```python
chr(87 % 26 + 97)
```




    'j'




```python
(ord('w') - 97 + 87) % 26 + 97
```




    102




```python
print(ord('a'), ord('b'), ord('c'), ord('f'), ord('w'), ord('x'), ord('y'), ord('z'))

print('A'.lower())
```

    97 98 99 102 119 120 121 122
    a



```python
#!/bin/python3

import math
import os
import random
import re
import sys

ORD_A_LOWER = ord('a')
ORD_Z_LOWER = ord('z')
COUNT_AZ = ORD_Z_LOWER - ORD_A_LOWER + 1

# Complete the caesarCipher function below.
def caesar_cipher(original_str, k):
    """
    COUNT_AZ = 26 
    if 'w':
    (ord('w') - ord('a') + k) % COUNT_AZ + ord('a') 

    """
    new_str = ""
    for char in original_str:
        is_upper = char.isupper()
        char = char.lower()
        ord_char = ord(char)
        if ORD_A_LOWER <= ord_char <= ORD_Z_LOWER:
            new_ord_char = (ord_char - ORD_A_LOWER + k) % COUNT_AZ + 97
            if is_upper:
                new_str += chr(new_ord_char).upper()
            else:
                new_str += chr(new_ord_char)
        else:
            new_str += char
    return new_str

if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesar_cipher(s, k)
    print(result)
    
#     fptr.write(result + '\n')

#     fptr.close()

```

    10
    www.abc.xy
    87
    fff.jkl.gh



```python

```
