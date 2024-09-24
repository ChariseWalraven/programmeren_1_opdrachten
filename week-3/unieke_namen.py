# example output
# De ontdubbelde lijst met namen is ["max", "marie", "mark", "linda"]

names = ["max", "max", "marie", "marie", "mark", "mark", "linda", "linda",]

deduplicated_names = []

for name in names:
    if name not in deduplicated_names:
        deduplicated_names.append(name)

print(f'De ontdubbelde lijst met namen is {deduplicated_names}')
