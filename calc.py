import unittest

def add(x,y):
    return x+y

def pow(x,y):
    if y == 0:
        return 1
    else:
        return x*pow(x,y-1)

class calcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,5),8)

if __name__ == '__main__':
    unittest.main()
