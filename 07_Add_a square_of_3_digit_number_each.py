# WAP that will take 3 digits from the user and add the square of each digit

num = input("Enter a 3 digit number: ")

sum_digit = sum(int(n)**2 for n in num)

print(f"The sum of square of each digit in given number {num} is {sum_digit}")