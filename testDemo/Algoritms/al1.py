def calculate_sum(n):
    if n <= 0:
        raise ValueError("Invalid input: n must be a positive integer.")

    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    try:
        sum = calculate_sum(n)
        print("The sum of all numbers from 1 to", n, "is", sum)
    except ValueError as e:
        print(e)