#prime number palindrome and factorial using recursive function

# primenumbercheck = int(input("Enter a number to check if it is prime or not: "))
# if primenumbercheck > 1:
#     for i in range(2, int(primenumbercheck/2) + 1):
#         if (primenumbercheck % i) == 0:
#             print(primenumbercheck, "is not a prime number")
#             break
#     else:
#         print(primenumbercheck, "is a prime number")


# palindromecheck = str(input("Enter a string to check if it is palindrome or not: "))
# if palindromecheck == palindromecheck[::-1]:
#     print(palindromecheck, "is a palindrome")
# else:
#     print(palindromecheck, "is not a palindrome")

factorialcheck = int(input("Enter a number to check its factorial: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of", factorialcheck, "is", factorial(factorialcheck))

factorial(factorialcheck)
