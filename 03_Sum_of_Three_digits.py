# WAP that will give you sum of three digits

n = input("Enter three digit number: ")

sum_digits = sum(int(x) for x in n)

print(sum_digits)