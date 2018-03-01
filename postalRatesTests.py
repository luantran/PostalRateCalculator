# from app import PostalRatesCalculator
from postalRatesCalculator import PostalRatesCalculator
from nose.tools import *
import unittest
from io import StringIO
from unittest.mock import patch

class PostalRatesTests(unittest.TestCase):

    def test01_invalid_number_of_args(self):
        args = []
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Usage: app.py -f <from_address> -t <to_address> -l <length in cm> "
                                        "-w <width in cm> -h <height in cm> -k <weight in kg> -p <post type>\n")

    def test02_sanity(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Xpresspost']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "24.68\n")
    #
    # def test03_valid_from_address_with_space(self):
    #     args = ['-f', 'H4R 1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Xpresspost']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "24.68\n")
    #
    # def test04_valid_from_address_lowercase(self):
    #     args = ['-f', 'h4r1j7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "20.66\n")
    #
    # def test05_valid_to_address_with_space(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X 1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "20.66\n")
    #
    # def test06_valid_to_address_lowercase(self):
    #     args = ['-f', 'H4R1J7', '-t', 'h2x1z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "20.66\n")
    #
    # def test07_valid_dimensions(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10.0', '-w', '10.0', '-h', '10.0', '-k', '2', '-p', 'Regular']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "20.66\n")
    #
    # def test08_valid_weight(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'Regular']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "20.66\n")
    #
    # def test09_valid_posttype_regular_lowercase(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'regular']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "20.66\n")
    #
    # def test10_valid_posttype_xpress(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'Xpresspost']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "24.68\n")
    #
    # def test11_valid_posttype_xpress_lowercase(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'xpresspost']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "24.68\n")
    #
    # def test12_valid_posttype_priority(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'Priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "36.10\n")
    #
    # def test13_valid_posttype_priority_lowercase(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "36.10\n")
    #
    # def test14_invalid_from_address_length_more_than7(self):
    #     args = ['-f', 'H4R1J7254', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")
    #
    #
    # def test15_invalid_from_address_length_7_without_space(self):
    #     args = ['-f', 'H4R1J72', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")
    #
    # def test16_invalid_to_address_length_more_than7(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z834', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")
    #
    # def test17_invalid_to_address_7_without_space(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z834', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")
    #
    # #TODO
    # def test18_invalid_negative_dimensions(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '-10', '-w', '-10', '-h', '-10', '-k', '2.0', '-p', 'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "\n")
    #
    #
    # def test18_invalid_length_non_numeric(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '-10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
    #             'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Length is not a number!\n")
    #
    # def test18_invalid_width_non_numeric(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '-10', '-h', '10', '-k', '2.0', '-p',
    #             'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Width is not a number!\n")
    #
    # def test18_invalid_height_non_numeric(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '-10', '-k', '2.0', '-p',
    #             'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Height is not a number!\n")
    #
    # #TODO
    # def test18_invalid_negative_weight(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
    #             'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "\n")
    #
    # def test18_invalid_negative_weight(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '-2.0', '-p',
    #             'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "\n")
    #
    # def test18_invalid_weight_non_numeric(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '-2.0', '-p',
    #             'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Weight is not a number!\n")
    #
    # def test18_invalid_maximum_weight_exceeded(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '-2.0', '-p',
    #             'priority']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Maximum weight exceeded!\n")
    #
    # def test18_invalid_post_type(self):
    #     args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '-2.0', '-p',
    #             'hello']
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         prc = PostalRatesCalculator(args)
    #         # prc.calculateRate()
    #         output = fake_out.getvalue()
    #         self.assertEqual(output, "Invalid post type!\n")
