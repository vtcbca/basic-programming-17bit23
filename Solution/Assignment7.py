def triangle_pattern_recursion(n, current=1):
    if current > n:
        return
    print(" " * (n - current) * 2, end="")
    print(" ".join(str(x) for x in range(1, 2 * current)))
    triangle_pattern_recursion(n, current + 1)

n = int(input("Enter the number of lines: "))
triangle_pattern_recursion(n)
