import unittest
from unittest.mock import patch

from user_iteration import user_iteration, user_iteration1



class TestUserIteration1(unittest.TestCase):

    input_string = '10'

    @patch('builtins.input', return_value=input_string)
    def test_user_iteration(self, mock_input):
        result = user_iteration1()
        self.assertEqual(result, 10)



if __name__=='__main__':
    unittest.main()