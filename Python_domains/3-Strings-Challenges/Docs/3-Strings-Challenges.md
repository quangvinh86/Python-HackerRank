## [Ex3_1: sWAP cASE](https://www.hackerrank.com/challenges/swap-case/problem) 
Cho một chuỗi S. Yêu cầu thực hiện chuyển định dạng chữ của chuỗi S.
Nếu chữ cái viết hoa --> chuyển thành chữ thường và ngược lại.

Ví dụ:
```
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

```

## [Ex3_2: String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem)
Trong Python, một chuỗi có thể chia nhỏ theo các delimiter (dấu phân cách)

**Example:**

```Python
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']

```
Nối lại các chuỗi cũng đơn giản:

```Python
>>> a = "-".join(a)
>>> print a
this-is-a-string 

```
Yêu cầu: Viết một function thực hiện chia chuỗi theo dấu space và nối lại chúng bằng dấu -

>this is a string   

>this-is-a-string

## [Ex3_3: What's Your Name?](https://www.hackerrank.com/challenges/whats-your-name/problem)

Nhập tên và họ của một người trên hai dòng khác nhau. Thực hiện in ra màn hình dòng chứ:

```
Hello **firstname** **lastname**! You just delved into python.
```

## [Ex3_4: Mutations](https://www.hackerrank.com/challenges/python-mutations/problem)

Chúng ta đã biết lists là mutable (có thể thay đổi) và tuples là immutable (không thể thay đổi).
Hãy tiếp tục tìm hiểu kỹ thông qua các ví dụ dưới đây.

Bạn có một chuỗi là immutable và bạn cần phải làm gì đó để thay đổi được nó.

> string = "abracadabra"

You can access an index by:

> print string[5]
> a

Điều gì sẽ xảy ra nếu bạn muốn gán một giá trị?

```python
>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```

Làm thế nào bạn sẽ tiếp cận này?
- Một giải pháp là chuyển đổi chuỗi sang một danh sách và sau đó thay đổi giá trị.

```Python
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

```
- Cách tiếp cận khác là cắt chuỗi và nối lại.

```Python
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
```

**Yêu cầu:**
Đọc vào một chuỗi và vị trí, ký tự cần thay thế.
Thực hiện thay thế dữ liệu.

**Input:**
```
abracadabra
5 k
```

**Output:**
abrackdabra


# [Ex3_5: Find a string](https://www.hackerrank.com/challenges/find-a-string/problem)
Đọc vào 2 chuỗi, chuỗi chính - chuỗi con. Tìm số lần xuất hiện của chuỗi con trong chuỗi chính (tính từ trái qua phải)

**Input:**

```
ABCDCDC
CDC

```

**Output:**
```
2
```


# [Ex3_6: String Validators](https://www.hackerrank.com/challenges/string-validators/problem)

Python chứa nhiều hàm built-in cho phép thực hiện xác thực các dữ liệu.
Có thể kiểm tra xem một chuỗi có chứa: ký tự abc, số,...

**str.isalnum() **
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
```Python

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

```

**str.isalpha() **
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

```Python
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
```

**str.isdigit() **
This method checks if all the characters of a string are digits (0-9).
```Python
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
```

**str.islower() **
This method checks if all the characters of a string are lowercase characters (a-z).
```Python
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
```

**str.isupper() **
This method checks if all the characters of a string are uppercase characters (A-Z).
```Python
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
```

### Yêu cầu
Nhận đầu vào là một chuỗi, in ra màn hình kết quả nếu chuỗi có chứa các điều kiện sau: 
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

 
## [EX3_7: Text Alignment](https://www.hackerrank.com/challenges/text-alignment/problem)
Trong Python, một chuỗi có thể canh trái, canh phải hoặc canh giữa.

**.ljust(width)**

This method returns a left aligned string of length width.
```

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  

```

**.center(width)**

This method returns a centered string of length width.

```
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----

```

**.rjust(width)**

This method returns a right aligned string of length width.

```
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
```

### Yêu cầu:
Nhập vào 1 số và in ra màn hình logo Hackerrank (H) theo như ví dụ.
**Input:**

```
5

```

**Output:**
```
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
```

## [Ex3_8: Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem)
Thư viện textwrap cung cấp hai phương thức: wrap(), fill(). Với cách hoạt động như sau:

textwrap.wrap(): Chia một đoạn văn bản (chuỗi) thành các dòng khác nhau với độ dài là width (mặc định 70). Cách chia dựa trên dấu space. Kết quả trả về là một list.
Lưu ý: Nếu đọc được witdh ký tự nhưng đoạn cuối cùng chưa đọc hết một từ --> chuỗi trả về sẽ lùi lại, trả về từ vị trí khoảng trắng gần nhất.

ví dụ: 

```Python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
>>> print([(value, len(value)) for value in textwrap.wrap(string, 8)])
[('This is', 7), ('a very', 6), ('very', 4), ('very', 4), ('very', 4), ('very', 4), ('long', 4), ('string.', 7)]

```
Giải thích: 
"This is " --> đoạn này có 8 ký tự, sau khi striP() --> còn 7 ký tự.
"a very v" --> đoạn này có 8 ký tự nhưng ký tự tiếp theo không phải khoảng trắng --> thụt lại đến vị trí khoảng trắng gần nhất. --> a very
"very ver" --> đoạn này có 8 ký tự nhưng ký tự tiếp theo không phải khoảng trắng --> thụt lại đến vị trí khoảng trắng gần nhất.  --> very


textwrap.fill(): tương tự như wrap(), phương thức fill() sẽ thực hiện trả về một chuối chứa các dòng.
Có thể hiểu như này cho nhanh fill() = "\n.joint(wrap()).

Ví dụ: 
```Python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
```

```Python
>>textwrap.fill(string,8) == "\n".join(textwrap.wrap(string, 8))
True
```

### Yêu cầu đề bài: 
Cho một chuỗi S và một số n. Thực hiện wrap chuỗi S thành một chuỗi khác như ví dụ: 

**Input:**
```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

```

**Output:**

```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ  
```

## [Ex3_9: Designer Door Mat](https://www.hackerrank.com/challenges/designer-door-mat/problem)

Tôi ghét nhất loại vẽ ra những cái hình như thế này :(
Và tôi không muốn tốn thời gian để làm nó. Các bạn đọc yêu cầu từ hackerrank và code để giải ở dưới đây:

```
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]
print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))

```
## [Ex3_10: String Formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem) 
Cho một số tự nhiên N, in ra màn hình các số từ 1 đến n theo các loại:
1. Decimal
2. Octal
3. Hexadecimal (capitalized - định dạng 4 số đầy đủ, thêm 0 phía trước)
4. Binary

Mỗi số in ra trên một dòng. Format mỗi số được in ra có độ dài bằng độ dài của số N ở dạng nhị phân và dấu cách.

**Input:**

```
17
```



```
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

```

## [Ex3_11](https://www.hackerrank.com/challenges/alphabet-rangoli/problem)

Lại một bài in chữ kỳ dị. 

Với một số n, --> tìm tương ứng trong bảng mã ascii, chữ thường.
In ra hình với dạng: a ở trung tâm và các chữ khác xung quanh như sau:
n = 3, dòng đầu tiên: ----c---- --> len("----c----") =  9, bỏ 1 chữ c --> 8 --> chia hai bên = 4 
4 = (n - 1) * 2 --> Đây là công thức in ra dấu -
c-b-a-b-c: a-b-c lật ngược lại thứ tự sẽ có c-b-a

tương tự với các ký tự khác
```
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

```

## [Ex3_12 Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem)

Cho bạn một chuỗi S, hãy viết hoa từng chữ trong S.
Ghi chú: Chỉ viết hoa chữ cái đầu tiên của chữ.

**Input:**
hello word

**Output**
Hello Word



