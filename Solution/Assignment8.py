def alphabet_pattern_recursion(n, current=1):
    if current > n:
        return
    print(" " * (n - current) * 2, end="")
    increasing = " ".join(chr(64 + x) for x in range(1, current + 1))
    decreasing = " ".join(chr(64 + x) for x in range(current - 1, 0, -1))
    print(increasing + " " + decreasing)
    alphabet_pattern_recursion(n, current + 1)

n = int(input("Enter the number of lines: "))
alphabet_pattern_recursion(n)
