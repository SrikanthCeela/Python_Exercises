'''
WAP to check whether the number is armstrong or not

An Armstrong number (also called a Narcissistic number) is a number 
that is equal to the sum of its digits each raised to the power of the number of digits in the number.
'''

def is_armstrong_num(num):
    num_str = str(num)      # Convert number to string
    n = len(num_str)        # Number of digits
    sum = 0
    for digit in num_str:
        sum += int(digit) ** n      # Add digit raised to power n
    return sum == num               # Check if sum equals original number

print(is_armstrong_num(371))

