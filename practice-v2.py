import timeit


def f1():
    return [x ** 2 for x in range(1, 21)]


def f2():
    def f3():
        x = 1
        count = 1
        while count <= 20:
            yield x ** 2
            x += 1
            count += 1

    return f3()








print(timeit.timeit(stmt='f1()', setup='from __main__ import f1', number=100000))
print(timeit.timeit(stmt='next(f2())', setup='from __main__ import f2', number=100000))
