# add imports
import unittest
import sysconfig as sys

# Class to contain all the Unit Test for Python
# the runner for the test is nosetest

class TddWithPython(unittest.TestCase):
    def test_python_env(self):
        self.assertEquals('posix', sys.os.name)

        

# this line is required for running the python code        
if __name__ == '__main__':
    unittest.main()