import sys
import getopt
from exceptions import Error, InputError

class PostalRatesCalculator:

    def __init__(self, argv):
        #raise InputError("No ")

        self.from_address = ''
        self.to_address = ''
        self.length = ''
        self.width = ''
        self.height = ''
        self.weight = ''
        self.post = ''

        try:
            opts, args = getopt.getopt(argv, "f:t:l:w:h:k:p:", ["from=", "to=","length=", "width=","height=", "weight=", "post="])
        except getopt.GetoptError:
            # raise InputError("Input Error")
            sys.exit(2)
        for opt, arg in opts:
            if opt in ('-f', "--from"):
                self.from_address = 'arg'
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

        if not (self.from_address or self.to_address or self.length or self.width or self.height or self.weight or self.post):
            print("Usage: app.py -f <from_address> -t <to_address> -l <length in cm> -w <width in cm> -h <height in cm> -k <weight in kg> -p <post type>")

    def calculateRate(self):
        return None

if __name__ == "__main__":
    prc = PostalRatesCalculator(sys.argv[1:])
