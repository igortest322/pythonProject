def is_palindrome(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        return True
    else:
        return False

if __name__ == "__main__":
    string = input("Enter a string: ")
    if is_palindrome(string):
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")