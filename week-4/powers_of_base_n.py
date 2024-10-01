upper_lim = int(input('Upper limit: '))
base = int(input('Base: '))

pows = [base ** i for i in range(upper_lim) if base ** i <= upper_lim]

for p in pows:
    print(p)
