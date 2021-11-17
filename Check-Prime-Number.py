# Task : Write a program that takes a number from the user
# and prints the result to check if it is a prime number.

n = int(input("Check your number is prime number ? : "))
for i in range(2, n):
    if n % i == 0:
        print(n, " is not prime number")
        break
    else:
        print(n, " is prime number")
        break