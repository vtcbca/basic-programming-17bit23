def pattern_while_loop(rows):
    i = 1
    while i <= rows:
        print("* " * i)
        i += 1

rows = int(input("Enter the number of rows: "))
pattern_while_loop(rows)
