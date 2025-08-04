# WAP that will reverse a 4 digit number. Also it checks whether the reversed is same as the given number

n = input("Enter a 4 digit number: ")

rev = n[::-1]

print(f"Given number is: {n}\nReversed number is: {rev}")

# check both are same or not

if rev == n:
    print("Both are Same")
else:
    print("BOTH ARE NOT SAME")

