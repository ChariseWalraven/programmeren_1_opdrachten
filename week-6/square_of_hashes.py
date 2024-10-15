def hash_square(num):
    row = "#" * num
    cols = "\n".join((row for _ in range(num)))
    print(cols)


hash_square(3)
print("\n")
hash_square(5)
