# coding challenge 1

'''p = float(input("Enter the principal : "))
t = float(input("Enter the time in years : "))
r = float(input("Enter the principal : "))

i = p*r*t/100;

print("Interest : " + str(i))'''

# coding challenge 2

'''l = ["biryani", 'pizza', 'pasta', 'phuchka', 'ice-cream']
print(l[2])
l.append('chicken')
l.insert(3, 'tacos')
print(l)
'''

# coding challenge 3
'''for i in range(5):
    print('I am a programmer')


def square():
    for i in range(1, 10):
        print(i ** 2)


square()'''

# coding challenge 4
'''

def calculate_bmi(new_weight, new_height):
    new_bmi = new_weight / (pow(new_height, 2))
    return new_bmi


weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_bmi(weight, height)
print(bmi)'''

# coding challenge 5


def divide(a, b):
    try:
        res = a / b

    except ZeroDivisionError:
        print("Division by zero not permitted")
        res = 0
    return res


# coding challenge 6



