def fibonacci_list_comprehension(terms):
    a, b = 0, 1
    sequence = [a]
    for _ in range(terms - 1):
        a, b = b, a + b
        sequence.append(a)
    return sequence

num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence (up to {num_terms} terms): {fibonacci_list_comprehension(num_terms)}")
