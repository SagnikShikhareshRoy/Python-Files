import unittest


def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


# exec('print(isEven(43))')


class TestIsEvenMethod(unittest.TestCase):

    def test_isEven1(self, x=5):
        self.assertFalse(isEven(x))

    def test_isEven2(self, x=6):
        self.assertTrue(isEven(x))

    def test_isEven3(self, x='hello'):
        self.assertRaises(TypeError, isEven, x)


if __name__ == '__main__':
    unittest.main()
