"""
Write a method to replace all spaces to %20
"""
import unittest
def urlify(value):
    result=value.strip().replace(" ","%20")
    return result
def urlify_without_replace(value):
    new_string=""
    for i in value:
        if i==" ":
            new_string=new_string+"%20"
        else:
            new_string=new_string+i
    return new_string
class URLIFY_TEST(unittest.TestCase):
    def test_url(self):
        self.assertEqual(urlify("M a"),"M%20a")
if __name__=="__main__":
    unittest.main()