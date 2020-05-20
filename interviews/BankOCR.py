# QueerCode London

import unittest
from pprint import pprint

hardcoded_numbers_list = [
    [" _ ",
     "| |",
     "|_|"],
    ["   ",
     "  |",
     "  |"],
    [" _ ",
     " _|",
     "|_ "],
    [" _ ",
     " _|",
     " _|"],
    ["   ",
     "|_|",
     "  |"],
    [" _ ",
     "|_ ",
     " _|"],
    [" _ ",
     "|_ ",
     "|_|"],
    [" _ ",
     "  |",
     "  |"],
    [" _ ",
     "|_|",
     "|_|"],
    [" _ ",
     "|_|",
     " _|"],
]

hardcoded_numbers = []

for hn in hardcoded_numbers_list:
    hardcoded_numbers.append("\n".join(hn))

def identify_numbers(input_string):
    result_numbers = ''
    lines = input_string.split('\n')

    for idx, char in enumerate(lines[0]):
        if (idx % 3 == 0):
            top = lines[0][idx:idx+3]
            switch = lines[1][idx:idx+3]
            bottom = lines[2][idx:idx+3]
            vanilla = lines[3]
            
            input_number = "\n".join([top, switch, bottom])
            #print(input_number)
            
            for hn_idx, hn in enumerate(hardcoded_numbers):
                print("hn: {}".format(hn_idx))
                print(hn)
                if (input_number == hn):
                    result_numbers += str(hn_idx)
    print(result_numbers)
    return result_numbers

class TestBank(unittest.TestCase):

    def test_1(self):
        case = '''    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
'''

        self.assertEqual(identify_numbers(case), '123456789')

        
      
if __name__ == '__main__':
    
    unittest.main()
