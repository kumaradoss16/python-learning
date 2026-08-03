def binary_string(current, n):
    if len(current) == n:
        print(current)
        return

    binary_string(current + "0", n)
    binary_string(current + "1", n)

binary_string("", 3)