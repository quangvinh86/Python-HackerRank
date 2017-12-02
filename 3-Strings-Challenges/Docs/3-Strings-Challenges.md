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

 
