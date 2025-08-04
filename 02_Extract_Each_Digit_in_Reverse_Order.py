'''
WAP to extract each digit from an integer in the reverse order

for example, if the given int is 7536,
the output shall be "6 3 5 7", with a space separating the digits
'''

n = input("enter any numbers: ")

y = n[::-1]

k = " ". join(y)

print(f"given number is {n},\nReversed number is {k}")
