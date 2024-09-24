abs_limit = int(input('Typ een positief geheel getal: '))

lower_limit = -1*abs_limit
excl_upper_limit = abs_limit + 1

for i in range(lower_limit, excl_upper_limit):
    if i != 0:
        print(i)
