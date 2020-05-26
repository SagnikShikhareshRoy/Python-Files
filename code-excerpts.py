# import sqlite3
#
#
# def main():
#     conn = sqlite3.connect('SAMPLE.db')
#     cursor = conn.cursor()
#
#     cursor.execute("drop table if exists ITEMS")
#
#     sql_statement = '''CREATE TABLE ITEMS
#     (item_id integer not null, item_name varchar(300),
#     item_description text, item_category text,
#     quantity_in_stock integer)'''
#
#     cursor.execute(sql_statement)
#
#     items = [(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3),
#              (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5),
#              (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
#              (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
#              (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
#              ]
#
#     # Add code to insert records to ITEM table
#     sql = '''
#     insert into items values(?, ?, ?, ?, ?)
#     '''
#     cursor.executemany(sql, items)
#     conn.commit()
#     try:
#         cursor.execute("select * from ITEMS")
#     except:
#         return 'Unable to perform the transaction.'
#     rowout = []
#     for row in cursor.fetchall():
#         rowout.append(row)
#     return rowout
#     conn.close()
#
#
# if __name__ == '__main__':
#     res = main()
#     print(res)
#
# # !/bin/python3
#
# import sys
# import os
# import sqlite3
#
#
# # Complete the function below.
#
# def main():
#     conn = sqlite3.connect('SAMPLE.db')
#     cursor = conn.cursor()
#
#     cursor.execute("drop table if exists ITEMS")
#
#     sql_statement = '''CREATE TABLE ITEMS
#     (item_id integer not null, item_name varchar(300),
#     item_description text, item_category text,
#     quantity_in_stock integer)'''
#
#     cursor.execute(sql_statement)
#
#     items = [(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3),
#              (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5),
#              (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
#              (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
#              (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
#              ]
#
#     try:
#         cursor.executemany("Insert into ITEMS values (?,?,?,?,?)", items)
#         cursor.executemany("update ITEMS set quantity_in_stock = ? where item_id = ?",
#                            [(4, 103),
#                             (2, 101),
#                             (0, 105)])
#         # Add code below to delete items
#
#         cursor.execute("select item_id from ITEMS")
#     except:
#         return 'Unable to perform the transaction.'
#     rowout = []
#     for row in cursor.fetchall():
#         rowout.append(row)
#     return rowout
#     conn.close()
#
#
# '''For testing the code, no input is required'''
#
# if __name__ == "__main__":
#
# import os
# import sys
#
#
# # Add circle class implementation here
# class Circle:
#     count = 0
#
#     def __init__(self, radius):
#         self.radius = radius
#         Circle.count += 1
#
#     @staticmethod
#     def getPi():
#         return 3.14
#
#     @staticmethod
#     def getCircleCount():
#         return Circle.count
#
#     def area(self):
#         return round(self.getPi() * self.radius * self.radius, 2)
#
#
# '''Check the Tail section for input/output'''
# if __name__ == "__main__":
#     with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#         res_lst = list()
#         circcount = list()
#         lst = list(map(lambda x: float(x.strip()), input().split(',')))
#         for radi in lst:
#             c = Circle(radi)
#             res_lst.append(str(c.getCircleCount()) + " : " + str(c.area()))
#         fout.write("{}".format(str(res_lst)))
#
# # !/bin/python3
#
# import sys
# import os
#
#
# def log(func):
#     def inner(*args, **kwdargs):
#         str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__, args, kwdargs)
#         return str_template + "\n" + str(func(*args, **kwdargs))
#
#     return inner
#
#
# # Add greet function definition here
# @log
# def average(n1, n2, n3):
#     return (n1 + n2 + n3) / 3
#
#
# '''Check the Tail section for input/output'''
# if __name__ == "__main__":
#     with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#         res_lst = list()
#         (a, b, c) = (map(lambda x: float(x.strip()), input().split(',')))
#         res_lst.append(average(a, b, c))
#         fout.write("{}".format(*res_lst))
#
# import os
# import sys
#
#
# # Add Circle class implementation here
# class Circle:
#     no_of_circles = 0
#
#     def __init__(self, radius):
#         self.radius = radius
#         Circle.no_of_circles += 1
#
#     @classmethod
#     def getCircleCount(self):
#         return Circle.no_of_circles
#
#     def area(self):
#         return round(3.14 * self.radius * self.radius, 2)
#
#
# '''Check the Tail section for input/output'''
# if __name__ == "__main__":
#     with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#         res_lst = list()
#         circcount = list()
#         lst = list(map(lambda x: float(x.strip()), input().split(',')))
#         for radi in lst:
#             c = Circle(radi)
#             res_lst.append(str(c.getCircleCount()) + " : " + str(c.area()))
#         fout.write("{}\n{}".format(str(res_lst), str(Circle.getCircleCount())))
#
# # !/bin/python3
#
# import sys
# import os
#
#
# class Celsius:
#
#     def __get__(self, instance, owner):
#         return 5 * (instance.fahrenheit - 32) / 9
#
#     def __set__(self, instance, value):
#         instance.fahrenheit = 32 + 9 * value / 5
#
#
# class Temperature:
#     celsius = Celsius()
#
#     def __init__(self, initial_f):
#         self.fahrenheit = initial_f
#
#
# t1 = Temperature(32)
# print(t1.celsius)
#
# if __name__ == "__main__":
#     with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#         res_lst = list()
#         t1 = Temperature(int(input()))
#         res_lst.append((t1.fahrenheit, t1.celsius))
#         t1.celsius = int(input())
#         res_lst.append((t1.fahrenheit, t1.celsius))
#         fout.write("{}\n{}".format(*res_lst))


# !/bin/python3

import sys


# # Define the function 'coroutine_decorator' below
# def coroutine_decorator(coroutine_func):

# # Define the coroutine function 'linear_equation' below
# @coroutine_decorator
# def linear_equation(a, b):


# Define 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)

        next(c)
        return c

    return wrapper


# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        res = a * (x ** 2) + b
        print('Expression, {}*x^2 + {}, with x being {} equals {}'.format(a, b, x, res))


# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True:
        x = yield
        equation1.send(x)
        equation2.send(x)


def main(x):
    n = numberParser()
    n.send(x)


if __name__ == "__main__":
    x = float(input())

    res = main(x);


