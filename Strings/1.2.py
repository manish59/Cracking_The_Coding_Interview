"""
Notes:
Usually permutations is the combination of the characters. So if you sort and compare the values it should return the same value
"""
import unittest
def check_strings_permutation(input1,input2):
    return sorted(input1)==sorted(input2)

class TestPermutiaton(unittest.TestCase):
    def test_permutation(self):
        self.assertEqual(check_strings_permutation("abc","cba"),True)
if __name__=="__main__":
    unittest.main()