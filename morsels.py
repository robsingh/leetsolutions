"""
Make a program, dollars.py that takes a number (as a command-line argument) and 
prints that number written as US dollars with cents.

$ python dollars.py 80
$80.00
$ python dollars.py .05
$0.05
Make sure the amount is always printed with exactly two numbers after the decimal point:

$ python dollars.py 3.048
$3.05
$ python dollars.py 5.5
$5.50
"""

import sys

def format_dollars(amount):
    """
    Format the given amount as US dollars with cents.
    Args:
        amount: amount to be formatted
    Returns: 
        formatted amount as a string.
    """
    try:
        # parse the input amount as a float
        amount = float(amount)

        # format the amount with two decimal places
        formatted_amount = "${:.2f}".format(amount)
        return formatted_amount
    except ValueError:
        return "Invalid Input!"
    

if __name__ == "__main__":
    # check if a number is provided as a command-line argument
    if len(sys.argv) == 2:
        amount = sys.argv[1]
        formatted_amount = format_dollars(amount)
        print(formatted_amount)
    else:
        print("Usage: python dollars.py [amount]")
