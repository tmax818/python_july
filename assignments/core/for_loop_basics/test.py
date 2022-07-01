import unittest
from unittest.mock import patch


class HelloWorldTest(unittest.TestCase):

    def setup(self):
        pass


    @patch('builtins.print')
    def test_hello_world(self, mock_print):
        print(mock_print)




if __name__ == '__main__':
    unittest.main()

print(dir(patch('sys.stdout')))