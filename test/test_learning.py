import unittest

import sysconfig as sys

class TddWithPython(unittest.TestCase):
    def test_python_env(self):
        self.assertEquals('posix', sys.os.name)
        
        
if __name__ == '__main__':
    unittest.main()