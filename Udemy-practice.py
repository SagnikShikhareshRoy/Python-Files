'''age = int(input("Age daal be : "))
if age == 18:
    print("can vote")
elif age < 18 or age !=18:
    print("cant vote")
else:
    print("maa chudao bhosdiwaalo")'''

'''l1 = [1, 2, 3, 4]
print(l1 * 2)

l2 = ['apple', 'oranges', 'mango']

print(l1 + l2)
print('apple' in l2)

print(len(l2))

l2.insert(1, "Peach")
print(l2)

print(l2.index('Peach', 1, 3))


# function
def func():
    print('laude laglis')


func()

# for loop
for x in range(2):
    func()

for x in l2:
    print(x)

for x in range(0, 21, 2):
    print(x)

# While loop
count = 0
while count < 10:
    print(count)
    count += 1
'''

'''def add(a, b):
    print(a + b)


add(9, 8)



def mul(a, b):
    return a * b


print(mul(9, 8))'''
'''import random

for x in range(5):
    print(random.randint(1, 6))'''

'''def div(a, b):
    return a/b

try:
    x = div(9, 1)
    print(x)
except ZeroDivisionError:
    print("fucked up by zero")
finally:
    print('No matter what, it is going to get executed')

'''
# file = open("demo.txt", 'r')
# file2 = open(r"C:\Users\Sagnik Shikharesh R\Desktop\demo2.txt", 'w')
# print(file.readable())
# print(file2.writable())
#
# var = file.readline()
# while var != "":
#     print(var)
#     file2.write(var)
#     var = file.readline()
#
# file.close()
# file2.close()
#
# file2 = open(r"C:\Users\Sagnik Shikharesh R\Desktop\demo2.txt", 'r')
# var = file2.read()
# print(var)
# file2.close()
#
# file2 = open(r"C:\Users\Sagnik Shikharesh R\Desktop\demo2.txt", 'a')
# file2.write("appended line")
# file2.close()


person1 = {
    "name": "John",
    "age": 32
}
person2 = {
    1: "John",
    2: 32
}
print(person2.get(3, "laude le lo"))

# l = [x for x in range(10) if x%2 == 0]
# print(l)
#
# x, y = [x for x in input("de de baba : ").split()]
# print(x,y)

number = [1, 2, 3]

string = "behnchod {x}-{2}-{2}".format(number[0], number[2], number[1], x=4)
print(string)

s1 = {1, 2, 'f', 2}
print(type(s1), type(person1))
s2 = set([1, 2, 2])
print(s2)
print(s1)

print(dir(person1))
#
# s1.remove(el) -> removes element
# s1.discard(el) -> use when not sure element there or not
# s1.pop -> u know

# Union
print(s1 | s2)
print(s1.union(s2, s1))

# Intersection
print(s1 & s2)
print(s1.intersection(s2, s1))

# difference
print(s1 - s2)
print(s1.difference(s2))

# frozenset
d = frozenset(s1)


p1 = dict({
    1:"john",
    2: "Laude"
})

print(p1[1])

p2 = dict()
print(p2)

p2.update({1:"l", 2:'f'})
print(p2)


print(p2)
