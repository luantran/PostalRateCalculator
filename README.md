# Assignment 2: Postal Rate Calculator

## Files
1. postalRatesCalculator.py -> The code for the postal calculator
2. postalRatesTests.py > The nose test file with all the unittests
3. data.csv -> A set of test data that is used by the calculator and test file

## Setup
First make sure you have python3 installed. Then install the following packages.
    pip install nose
    pip install mock

Then to run the calculator command line program
    python3 postalRatesCalculator.py [args]

An example run would be...
    python3 postalRatesCalculator.py -f H4R1J7 -t H2X1Z8 -l 10.0 -w 10.0 -h 10.0 -k 2.0 -p Priority
