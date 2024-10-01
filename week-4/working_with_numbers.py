nums = []
num = None

print('Please type in integer numbers. Type in 0 to finish.')
while num != 0:
    if num is not None:
        nums.append(num)

    num = int(
        input('Number: ')
    )
else:
    nums_ln = len(nums)
    nums_sum = sum(nums)
    nums_mean = nums_sum / nums_ln
    nums_pos = len([num for num in nums if num > -1])
    nums_neg = len([num for num in nums if num < 0])
    print(
        f'Numbers typed in {nums_ln}',
        f'The sum of the numbers is {nums_sum}',
        f'The mean of the numbers is {nums_mean}',
        f'Positive numbers {nums_pos}',
        f'Negative numbers {nums_neg}',
        sep='\n',
    )
