def is_palindrome_recursion(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursion(s[1:-1])

input_str = input("Enter a string: ").lower()
if is_palindrome_recursion(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
