import unittest

def NWD(a, b):
    if a == b:
        return a
    elif a > b:
        return NWD(a - b, b)
    else:
        return NWD(a, b - a)
        
class TestNWDFunction(unittest.TestCase):

    def test_same_numbers(self):
        result = NWD(5, 5)
        self.assertEqual(result, 5)

    def test_a_greater_than_b(self):
        result = NWD(12, 8)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
