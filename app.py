import sys
import getopt
import csv


class PostalRatesCalculator:
    def __init__(self, argv):
        # raise InputError("No ")

        self.from_address = ''
        self.to_address = ''
        self.length = ''
        self.width = ''
        self.height = ''
        self.weight = ''
        self.post = ''

        try:
            opts, args = getopt.getopt(argv, "f:t:l:w:h:k:p:",
                                       ["from=", "to=", "length=", "width=", "height=", "weight=", "post="])
        except getopt.GetoptError:
            # raise InputError("Input Error")
            sys.exit(0)
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

        if not (self.from_address and self.to_address and self.length and self.width and
                    self.height and self.weight and self.post):
            print("Usage: app.py -f <from_address> -t <to_address> -l <length in cm> -w <width in cm> "
                  "-h <height in cm> -k <weight in kg> -p <post type>")
            sys.exit(0)
        self.validateInputs()
        self.calculateRate()

    def validateInputs(self):
        self.from_address = self.checkPostalCode(self.from_address)
        self.to_address = self.checkPostalCode(self.to_address)
        dict = self.checkDimensions(self.length, self.height, self.width)
        self.length = dict['Length']
        self.height = dict['Height']
        self.width = dict['Width']
        self.weight = self.checkWeight(self.weight)
        self.post = self.checkPostType(self.post)

    def checkPostalCode(self, postal_code):
        postal_code = postal_code.upper()
        if len(postal_code) == 7:
            if " " in postal_code:
                postal_code = postal_code.split(" ")[0] + postal_code.split(" ")[1]
            else:
                print("Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3")
                sys.exit(0)

        if len(postal_code) == 6:
            if not (postal_code[0].isalpha() and postal_code[1].isdigit() and postal_code[2].isalpha() and postal_code[
                3].isdigit() and
                        postal_code[4].isalpha() and postal_code[5].isdigit()):
                print("Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3")
                sys.exit(0)
        else:
            print("Invalid postal code format! Please input the following format: A1B2C3 or A1B 2C3")
            sys.exit(0)
        return postal_code

    def checkDimensions(self, length, height, width):
        dict = {'Length':length, 'Height': height, 'Width': width}
        for key, value in dict.items():
            try:
                dict[key] = float(value)
            except ValueError:
                print(key + " is not a number!")
                sys.exit(0)
        return dict

    def checkWeight(self, weight):
        try:
            weight = float(weight)
        except ValueError:
            print("Weight is not a number")
            sys.exit(0)
        if float(weight) > 30:
            print("Maximum weight exceeded!")
        return weight

    def checkPostType(self, post):
        post = post.lower().title()
        types = ['Regular', 'Xpresspost', 'Priority']
        if post not in types:
            print("Invalid post type!")
            sys.exit(0)
        return post

    def calculateRate(self):
        reader = csv.DictReader(open('data.csv'))
        rate = ''
        for row in reader:
            if self.from_address == row['from'] and self.to_address == row['to']:
                if self.length == float(row['length']) and self.width == float(row['width']) and self.height == float(row['height']) and self.weight == float(row['weight']):
                    if self.post == row['post']:
                        rate = row['rate']
        if rate:
            print(rate)
        else:
            print("No rates found!")

if __name__ == "__main__":
    prc = PostalRatesCalculator(sys.argv[1:])
    # prc.calculateRate()
    # prc.printAll()
