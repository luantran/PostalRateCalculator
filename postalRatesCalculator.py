import sys
import getopt
import csv

class PostalRatesCalculator:
    def __init__(self):
        self.from_address = ''
        self.to_address = ''
        self.length = ''
        self.width = ''
        self.height = ''
        self.weight = ''
        self.post = ''

    def getRate(self, argv):
        try:
            opts, args = getopt.getopt(argv, "f:t:l:w:h:k:p:",
                                       ["from=", "to=", "length=", "width=", "height=", "weight=", "post="])
        except getopt.GetoptError:
            print("Usage: app.py -f <from_address> -t <to_address> -l <length in cm> -w <width in cm> "
                  "-h <height in cm> -k <weight in kg> -p <post type>")
            return False
        for opt, arg in opts:
            if opt in ('-f', "--from"):
                self.from_address = arg
            elif opt in ("-t", "--to"):
                self.to_address = arg
            elif opt in ("-l", "--length"):
                self.length = arg
            elif opt in ("-w", "--width"):
                self.width = arg
            elif opt in ("-h", "--height"):
                self.height = arg
            elif opt in ("-k", "--weight"):
                self.weight = arg
            elif opt in ("-p", "--post"):
                self.post = arg
            else:
                print("Usage: postalRatesCalculator.py -f <from_address> -t <to_address> -l <length in cm> -w <width in cm> "
                      "-h <height in cm> -k <weight in kg> -p <post type>")


        if not (self.from_address and self.to_address and self.length and self.width and
                    self.height and self.weight and self.post):
            print("Usage: postalRatesCalculator.py -f <from_address> -t <to_address> -l <length in cm> -w <width in cm> "
                  "-h <height in cm> -k <weight in kg> -p <post type>")
            return False

        if not self.validateInputs():
            return False

        self.searchRate()

    def validateInputs(self):
        self.from_address = self.checkPostalCode(self.from_address)
        if not self.from_address:
            return False
        self.to_address = self.checkPostalCode(self.to_address)
        if not self.to_address:
            return False
        self.post = self.checkPostType(self.post)
        if not self.post:
            return False

        if not self.checkDimensions(self.length, self.height, self.width):
            return False

        if not self.checkWeight(self.weight):
            return False
        return True

    def checkPostalCode(self, postal_code):
        postal_code = postal_code.upper()
        if len(postal_code) == 7:
            if " " in postal_code:
                postal_code = postal_code.split(" ")[0] + postal_code.split(" ")[1]
            else:
                print("Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3")
                return False
        if len(postal_code) == 6:
            if not (postal_code[0].isalpha() and postal_code[1].isdigit() and postal_code[2].isalpha() and postal_code[
                3].isdigit() and
                        postal_code[4].isalpha() and postal_code[5].isdigit()):
                print("Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3")
                return False
        else:
            print("Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3")
            return False
        return postal_code

    def checkDimensions(self, length, height, width):
        dict = {'Length': length, 'Height': height, 'Width': width}
        count = 0
        output = ''
        for key, value in dict.items():
            try:
                dict[key] = float(value)
            except ValueError:
                count += 1
                output = "Invalid input: " +key + " is not a number!"
        if count == 0:
            return self.checkNegativeNumber(dict)
        elif count > 1:
            print("Invalid input: Dimensions are not numbers!")
            return False
        else:
            print(output)
            return False

    def checkNegativeNumber(self, dict):
        count = 0
        output = ''
        for key, value in dict.items():
            if value < 0:
                count += 1
                output = "Invalid input: "+key+" is negative!"
        if count == 0:
            return True
        elif count > 1:
            print("Invalid input: Negative dimensions!")
            return False
        else:
            print(output)
            return False

    def checkWeight(self, weight):
        try:
            weight = float(weight)
            if weight < 0:
                print("Invalid input: Weight is negative!")
                return False
        except ValueError:
            print("Invalid input: Weight is not a number!")
            return False
        if weight > 30:
            print("Invalid input: Maximum weight exceeded!")
            return False
        return True

    def checkPostType(self, post):
        post = post.lower().title()
        types = ['Regular', 'Xpresspost', 'Priority']
        if post not in types:
            print("Invalid post type!")
            return False
        return post

    def searchRate(self):
        reader = csv.DictReader(open('data.csv'))
        rate = ''
        for row in reader:
            if self.from_address == row['from'] and self.to_address == row['to']:
                if float(self.length) == float(row['length']) and float(self.width) == float(row['width']) and \
                                float(self.height) == float(row['height']) and float(self.weight) == float(row['weight']):
                    if self.post == row['post']:
                        rate = row['rate']
        if rate:
            print(rate)
        else:
            print("No rates found!")

if __name__ == "__main__":
    prc = PostalRatesCalculator()
    prc.getRate(sys.argv[1:])

