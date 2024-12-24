def factorial_while_loop(n):
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial

num = int(input("Enter a number: "))
print(f"Factorial using while loop: {factorial_while_loop(num)}")
