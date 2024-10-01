num = int(input('Please type in a number:'))

nums = range(1, num + 1)

combinations = [f'{n} x {nn} = {n * nn}' for n in nums for nn in nums]

print(*combinations, sep='\n')
