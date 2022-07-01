import unittest
from unittest.mock import patch


class HelloWorldTest(unittest.TestCase):

    def setup(self):
        import hello_world 

    @patch('builtins.print')
    def test_hello_world(self, mock_print):
        import hello_world 
        mock_print.assert_called_with("Hello World")




if __name__ == '__main__':
    unittest.main()
