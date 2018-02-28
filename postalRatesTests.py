from app import PostalRatesCalculator
from nose.tools import *
import unittest
from exceptions import InputError
from io import StringIO
from unittest.mock import patch

class PostalRatesTests(unittest.TestCase):

    # @raises(InputError)
    def test_valid_number_of_args(self):
        args = []
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator(args)
            output = fake_out.getvalue()
            # self.assertNotIn("Missing Arguments", output)
            self.assertNotEqual(output, "Usage: app.py -f <from_address> -t <to_address> -l <length in cm> "
                                        "-w <width in cm> -h <height in cm> -k <weight in kg> -p <post type>\n")
            # self.assertEqual(fake_out.getvalue(), "")

    def test_valid_from_address(self):
        args = []
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator(args)
            # self.assertEqual(fake_out.getvalue(), "")



