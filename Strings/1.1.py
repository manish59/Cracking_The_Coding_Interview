import unittest
def string_unique(string):
    checker=0 
    for i in string:
        val=ord(i)-ord('a') 
        print('{:032b}'.format(checker))
        print('{:032b}'.format(1<<val))
        print('{:032b}'.format(checker & (1<<val)))
        print(checker & (1<<val))
        if (checker & (1<<val))>0:
            return(False)
        checker |= (1<<val)  # 1 represent one bit and << represent shifting that many values to the left
                            # and | is like adding or flipping the bits and we are storing all the bits
    return(True)
class Test_Is_Unique(unittest.TestCase):
    def test_without_datastructures(self):
        self.assertEqual(string_unique("manish"),True)
    def test_not_unique(self):
        self.assertEqual(string_unique("manisha"),False)
if __name__=="__main__":
    unittest.main()