def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
