def reverse_string_recursion(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string_recursion(s[:-1])

input_str = input("Enter a string: ")
print(f"Reversed string (using recursion): {reverse_string_recursion(input_str)}")
