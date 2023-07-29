import unittest

def is_even(number):
        if number % 2 == 0:
            print(True)
        else:
            print(False)
#Returns True if number is even or False if it is odd.
        return number % 2

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())

    def test_split(self):
        test = "test split"
        self.assertEqual(test.split(), ["test", "split"])

        with self.assertRaises(TypeError):
            test.split(2)

if __name__ == "__main__":
    unittest.main()