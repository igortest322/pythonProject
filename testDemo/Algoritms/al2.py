def factorial(n):
    if n < 0:
        raise ValueError("Invalid input: n must be a non-negative integer")

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    try:
        result = factorial(n)
        print("The factorial of", n, "is", result)
    except ValueError as e:
        print(e)