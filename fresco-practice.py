import itertools as it
import math

"""name = input("naam bol be :")
"""
'''help(input)'''

x = 6
y = 12
m = '0b1011'
n = 0xad4

print(type(x))
print(type(y))
print(type(m))
print(type(n))

print(x == y)

wel = "laude"
print(wel.isdigit())

x = bytearray('abcd', 'utf-8')
print(x[0])
x[0] = 68
print(x)
x.decode("utf-8")

emplist1 = []
print(emplist1)
emplist1.append(2)
del (emplist1[-1])
e = emplist1
print(emplist1)

tup = tuple(['welcome'])
print(tup[0].count("e"))

list1 = [1, 2, 3, 4, 5, 6, 7]

print(list1[0:3:2])

list1[0] = 'j'
print(list1)
tup = ('c', 'b')
print(tup)
# tup[0]='c'
print(tup[0])

print(tup)

print(max('Infinity'))

list2 = [*range(10, 20, 2)]
print(list2)

k4 = [*range(100, 1, -25)]
print(k4)

s = 'tata consultancy ltd'
count = 0
i = len(s) - 1
while i >= 0:
    if s[i] == 'a':
        count += 1
    i -= 1
print(count)

count = 0

for j in range(i):
    if s[j] == 'a':
        count += 1
print(count)

g = 68.3
g = round(g)
if g in range(60, 90):
    print(g)

k = range(60, 90)

st = 'laude'
st = reversed(st)
st = ''.join(st)
print(st)

print(st[-1::-1])
a = list()
print(a)
x, y = 5, 6
print(bool(0))

st = 'laude'
iter1 = iter(st)
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break;


def gen():
    r = 5 + 2

    yield 1
    yield 2
    return r


x = gen()
print(type(gen()))  # --> <class 'generator'>
print(type(gen))  # --> <class 'function'>

print(x)
# for i in x:
#     print(i)
print(x)

zenPython = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

print(zenPython)

words = zenPython.split()
print(words)

words[0].strip()

words = [x.strip(', . - * ! ') for x in words]
print(words)

words = [x.lower() for x in words]
print(words)

print(len(words))
set_words = set(words)
print(len(set_words))
# words.count()

word_frequency = {x: words.count(x) for x in set(words)}
print(word_frequency)

frequent_words = {x: words.count(x) for x in word_frequency if words.count(x) > 5}
print(len(frequent_words))


def fib_gen():
    a = 0
    b = 1
    while True:
        c = a + b
        a = b
        b = c
        yield c


fs = fib_gen()
print(next(fs))
print(next(fs))
print(next(fs))


def factorial_gen():
    a = 1
    yield a
    yield a
    while True:
        a *= (a + 1)
        yield a


fs = factorial_gen()
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))

# fs.
print(type(id(fs)))

k = [print(i) for i in "maverick" if i not in "aeiou"]


# print(k)

class Person:
    def __init__(self, fname, lname):
        """ initialising content """
        self.fname = fname
        self.lname = lname


p1 = Person('George', 'Smith')
print(p1.fname, '-', p1.lname)


# help(Person)

class Person:
    """laudeya"""

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class Employee(Person):
    all_employees = []

    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)


p1 = Person('George', 'smith')
print(p1.fname, '-', p1.lname)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('John', 'williams', 123656)
print(e1.fname, '-', e1.empid)
print(e2.fname, '-', e2.empid)


class grandpa(object):
    pass


class father(grandpa):
    pass


class mother(object):
    pass


class child(mother, father):
    pass


print(child.__mro__)


class A:
    def __init__(self, a=5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b=0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10


x = B()
x.f1()
print(x.a, '-', x.b)


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        s = "point : (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ')'
        return s

    def distance(self, p2):
        distance = math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2 + (self.z - p2.z) ** 2)
        return distance

    def __add__(self, p2):
        self.x += p2.x
        self.y += p2.y
        self.z += p2.z
        return self


p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)
print(p2 + p3)
print(p2.distance(p3))

p1 = Point(4, 2, 9)
print(p1)


def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


exec('print(isEven(43))')

try:
    a = 2;
    b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise TypeError('Two inputs must be integers.')
    c = a ** b
except TypeError as e:
    print(e)
except ValueError:
    print()


class CustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


try:
    a = 2;
    b = 'hello'
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CustomError('Two inputs must be integers.')
        c = a ** b
except CustomError as e:
    print(e)

try:
    a = 14 / 7
except ZeroDivisionError:
    print('oops!!!')
else:
    print('First ELSE')
try:
    a = 14 / 0
except ZeroDivisionError:
    print('oops!!!')
else:
    print('Second ELSE')


# try:
#     p = input("Enter a string of length 10 :")
#     if len(p) > 10:
#         raise ValueError("Input String contains more than 10 characters.")
# except ValueError as v:
#     print(v)


class Custom(FileNotFoundError):
    def __str__(self):
        print("File not found.")


try:
    p = open("unknown_file.txt", "r")
except FileNotFoundError:
    print("File not found.")


class Custom(FileNotFoundError):
    def __str__(self):
        print("File not found.")


class RadiusInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Circle:
    def __init__(self, radius):
        self.radius = radius


try:
    c1 = Circle('hello')
    if not (isinstance(c1, float) or isinstance(c1, int)):
        raise RadiusInputError("'" + c1.radius + "' is not a number")
except RadiusInputError as r:
    print(r)

a = [1, 2, 2]

print('2' == 2)


def even_or_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'


n = [10, 14, 16, 22, 9, 3, 37]
nl = []
for x in n:
    nl.append((even_or_odd(x), x))

print(nl)
c = it.groupby(nl, lambda x: x[0])
# print(c)
for key, group in c:
    print(key, list(group), sep=': ')

import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if name.endswith('.py'):
            print(name)

# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))
#
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(name)
#     for name in dirs:
#         print(os.path.join(root))
#


import calendar
import datetime


def month_name_getter(x):
    month_number = x
    datetime_object = datetime.datetime.strptime(month_number, "%m")
    month_name = datetime_object.strftime("%b")
    return month_name


year = 2018

obj = calendar.Calendar(firstweekday=6)
count = 0

for month in range(1, 13):
    count = 0
    for day in obj.itermonthdays2(year, month):
        i = list(day)
        if i[0] != 0 and i[1] == 6:
            count += 1
    if count > 4:
        print(month_name_getter(str(month)))


# full_month_name = datetime_object.strftime("%B")
# print(full_month_name)


def f2():
    # this is also a generator
    g = (x ** 2 for x in range(1, 200001))
    return g


import pstats, cProfile


def f1(n1):
    f = [i ** 2 for i in range(1, n1)]
    return f


def f2(n2):
    g = (x ** 2 for x in range(1, n2))
    return g


cProfile.runctx("f1(n1)", globals(), {'n1': 200001}, "Profile1.prof")
cProfile.runctx("f2(n2)", globals(), {'n2': 200001}, "Profile2.prof")

s1 = pstats.Stats("Profile1.prof")
s1.strip_dirs().sort_stats("time").print_stats()

s2 = pstats.Stats("Profile2.prof")
s2.strip_dirs().sort_stats("time").print_stats()

print([(i.upper(), len(i)) for i in 'kiwi'])

import io


def main():
    zenPython = '''
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    '''
    fp = io.StringIO(zenPython)

    zenlines = fp.readlines()

    for i in range(len(zenlines)):
        zenlines[i] = zenlines[i].strip()
    print(zenlines)


if __name__ == '__main__':
    main()

import re

pattern = '-[\w|\s]+-'
pattern2 = '\*[\w|\s]+\*'
print(re.findall(pattern, zenPython))
print(re.findall(pattern2, zenPython))

x = [x.strip("-* ") for x in re.findall(pattern, zenPython)]
print(x)

pattern1 = '-[\w|\s]+-'
pattern2 = '\*[\w|\s]+\*'
portions = [x.strip("-* ") for x in re.findall(pattern1, zenPython)]
portions2 = [x.strip("-* ") for x in re.findall(pattern2, zenPython)]

portions2.append(portions[0])

# temp = re.findall(pattern2, zenPython)
# print(temp)
# portions.append(x for x in temp)
print(portions)
print(portions2)

# Add portions implementation here
# portions = [x.strip("-* ") for x in portions]


# from abc import ABC, abstractmethod
#
# class A(ABC):
#
#     @classmethod
#     @abstractmethod
#     def m1(self):
#         print('In class A, Method m1.')
#
# class B(A):
#
#     @classmethod
#     def m1(self):
#         print('In class B, Method m1.')
#
# b = B()
# b.m1()
# B.m1()
# A.m1()
#
# import zipfile
# import sys
# import os
# import inspect
#
#
# # Define 'writeTo' function below, such that
# # it writes input_text string to filename.
# def writeTo(filename, input_text):
#     with open(filename, 'w') as fp:
#         fp.write(input_text)
#
#
# # Define the function 'archive' below, such that
# # it archives 'filename' into the 'zipfile'
# def archive(zfile, filename):
#     with zipfile.ZipFile(zfile, 'w') as zipf:
#         zipf.write(filename)
#
#
# if __name__ == "__main__":
#     try:
#         filename = str(input())
#     except:
#         filename = None
#
#     try:
#         input_text = str(input())
#     except:
#         input_text = None
#
#     try:
#         zip_file = str(input())
#     except:
#         zip_file = None
#
#     res = writeTo(filename, input_text)
#
#     if 'with' in inspect.getsource(writeTo):
#         print("'with' used in 'writeTo' function definition.")
#
#     if os.path.exists(filename):
#         print('File :', filename, 'is present on system.')
#
#     res = archive(zip_file, filename)
#
#     if 'with' in inspect.getsource(archive):
#         print("'with' used in 'archive' function definition.")
#
#     if os.path.exists(zip_file):
#         print('ZipFile :', zip_file, 'is present on system.')
#

def TokenIssuer():
    tokenId = 0
    while True:
        name = yield
        tokenId += 1
        print('Token number of', name, ':', tokenId)
t = TokenIssuer()
next(t)

t.send('George')
t.send('Rosy')
t.send('Smith')


print(re.sub('[a-z]', 'X', 'abcdefghij'))

from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def m1(self):
        print('In class A, Method m1.')

class B(A):

    @staticmethod
    def m1(self):
        print('In class B, Method m1.')

b = B()
B.m1(b)

# class A:
#
#     def __init__(self, value):
#         self.x = value
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError('Only Int or float is allowed')
#         self.__x = value
#
# a = A(7)
# a.x = 'George'
# print(a.x)

# class A:
#
#     def __init__(self, x):
#         self.__x = x
#
#     @property
#     def x(self):
#         return self.__x
#
# a = A(7)
# a.x = 10
# print(a.x)





from contextlib import contextmanager

@contextmanager
def context():
    print('Entering Context')
    yield
    print("Exiting Context")

with context():
    print('In Context')


n = 'laude'
print(type(n[-1::-1]))

import inspect

#!/bin/python3

import math
import os
import random
import re
import sys
import inspect



def isPalindrome(x):
    # Write the doctests:
    """
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
    ValueError:x must be a positive integer
    >>> isPalindrome("hello")
    Traceback (most recent call last):
    TypeError: x must be an integer
    """
    # Write the functionality:
    try:
        if isinstance(x, str):
            raise TypeError('Traceback (most recent call last):\nTypeError: x must be an integer')
        elif x < 0:
            raise ValueError('Traceback (most recent call last):\nValueError:x must be a positive integer')
        elif isinstance(x,int) and x >= 0:
            string = str(x)
            rev = string[-1::-1]
            if string == rev:
                return 'True'
            return 'False'
    except Exception as e:
       return e


if __name__ == '__main__':
    fptr = open('file.txt','w')

    x = input()

    if x.isdigit():
        x = int(x)

    res = isPalindrome(x)

    doc = inspect.getdoc(isPalindrome)

    func_count = len(re.findall(r'isPalindrome', doc))
    true_count = len(re.findall(r'True', doc))
    false_count = len(re.findall(r'False', doc))
    pp_count = len(re.findall(r'>>>', doc))
    trace_count = len(re.findall(r'Traceback', doc))

    fptr.write(str(res) + '\n')
    fptr.write(str(func_count) + '\n')
    fptr.write(str(true_count) + '\n')
    fptr.write(str(false_count) + '\n')
    fptr.write(str(pp_count) + '\n')
    fptr.write(str(trace_count) + '\n')

    fptr.close()

    fptr = open('file.txt','r')
    print(fptr.readlines())
    fptr.close()
# def isPalindrome(x):
#     n = x
#     res = 0
#     while n > 0:
#         temp = n % 10
#         temp1 = n // 10
#         n = temp1
#         res = res*10 + temp
#     if res == x:
#         return True
#     else:
#         return False

