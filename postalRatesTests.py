# from app import PostalRatesCalculator
from postalRatesCalculator import PostalRatesCalculator
from nose.tools import *
import csv
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
            self.assertEqual(output, "Usage: postalRatesCalculator.py -f <from_address> -t <to_address> -l <length in cm> "
                                        "-w <width in cm> -h <height in cm> -k <weight in kg> -p <post type>\n")

    def test02_sanity(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

    def test03_valid_from_address_with_space(self):
        args = ['-f', 'H4R 1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

    def test04_valid_from_address_lowercase(self):
        args = ['-f', 'h4r1j7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

    def test05_valid_to_address_with_space(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X 1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

    def test06_valid_to_address_lowercase(self):
        args = ['-f', 'H4R1J7', '-t', 'h2x1z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

    def test07_valid_dimensions_floating_points(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10.5', '-w', '10.5', '-h', '10.5', '-k', '2', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

    def test08_valid_weight_floating_point(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '5', '-w', '5', '-h', '5', '-k', '2.5', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.40\n")

    def test09_valid_posttypes(self):
        prc = PostalRatesCalculator()
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'Xpresspost']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "16.37\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'Priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "25.84\n")

    def test10_valid_posttype_lowercase_uppercase(self):
        prc = PostalRatesCalculator()
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'REGULAR']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "13.11\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'xpresSpost']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "16.37\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "25.84\n")

    def test11_invalid_addresses_length_7_without_space(self):
        args = ['-f', 'H4R1J72', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: "
                                     "A1B2C3 or A1B 2C3\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X14Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: "
                                     "A1B2C3 or A1B 2C3\n")


    def test12_invalid_addresses_incorrect_format_correct_length(self):
        args = ['-f', '123456', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")

        args = ['-f', 'H4R1J7', '-t', 'A4576B', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")


    def test13_invalid_addresses_length_more_than7(self):
        args = ['-f', 'H4R1J7A4F', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z85F5', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")

        args = ['-f', 'H4R1J7F5', '-t', 'H2X1Z85F5', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")

    def test14_invalid_addresses_less_than_6(self):
        args = ['-f', 'H4R', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")
        args = ['-f', 'H4R1J7', '-t', 'H', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")

        args = ['-f', '5', '-t', 'H', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output,
                             "Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3\n")

    def test15_invalid_dimensions_non_numeric(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', 'afsa', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Length is not a number!\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', 'asj', '-h', '10', '-k', '2.0', '-p',
                'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Width is not a number!\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '%^', '-k', '2.0', '-p',
                'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Height is not a number!\n")

    def test16_invalid_multiple_dimensions_non_numeric(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', 'adfh', '-w', '87hj', '-h', '%^', '-k', '2.0', '-p',
                'Regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Dimensions are not numbers!\n")

    def test17_invalid_negative_dimensions(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '-10', '-w', '10', '-h', '10', '-k', '2.0', '-p', 'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Length is negative!\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '-10', '-h', '10', '-k', '2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Width is negative!\n")

        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '-10', '-k', '2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Height is negative!\n")

    def test18_invalid_multiple_negative_dimensions(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '-10', '-w', '-10', '-h', '-10', '-k', '2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Negative dimensions!\n")

    def test19_invalid_weight_non_numeric(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', 'hello', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Weight is not a number!\n")


    def test20_invalid_negative_weight(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '-2.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Weight is negative!\n")


    def test21_invalid_maximum_weight_exceeded(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '34.0', '-p',
                'priority']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid input: Maximum weight exceeded!\n")

    def test22_invalid_post_type(self):
        args = ['-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'hello']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Invalid post type!\n")

    def test23_too_many_args(self):
        args = ['hello','-f', 'H4R1J7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Usage: postalRatesCalculator.py -f <from_address> -t <to_address> -l <length in cm> "
                                        "-w <width in cm> -h <height in cm> -k <weight in kg> -p <post type>\n")

        args = ['-f', 'H4R1J7', 'hello', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "Usage: postalRatesCalculator.py -f <from_address> -t <to_address> -l <length in cm> "
                                        "-w <width in cm> -h <height in cm> -k <weight in kg> -p <post type>\n")
    def test24_no_rates(self):
        args = ['-f', 'V4R1H7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p',
                'regular']
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prc = PostalRatesCalculator()
            prc.getRate(args)
            output = fake_out.getvalue()
            self.assertEqual(output, "No rates found!\n")

    def test25_variable_inputs_sanity(self):
        args = ['-f', 'V4R1H7', '-t', 'H2X1Z8', '-l', '10', '-w', '10', '-h', '10', '-k', '2.0', '-p','regular']
        with open('data.csv', 'r') as f:
            next(f)
            reader = csv.reader(f)
            for row in reader:
                input_args = ['-f', row[0], '-t', row[1], '-l', row[2], '-w', row[3], '-h', row[4], '-k', row[5], '-p', str.lower(row[6])]

                with patch('sys.stdout', new=StringIO()) as fake_out:
                    prc = PostalRatesCalculator()
                    prc.getRate(input_args)
                    output = fake_out.getvalue()
                    self.assertEqual(output, row[7]+"\n")

