def is_prime_list(n):
    if n <= 1:
        return False
    divisors = [i for i in range(2, int(n**0.5) + 1) if n % i == 0]
    return len(divisors) == 0

num = int(input("Enter a number: "))
print(f"{num} is {'a prime' if is_prime_list(num) else 'not a prime'} number.")
