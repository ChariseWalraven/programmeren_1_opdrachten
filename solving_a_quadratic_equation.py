# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt


a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))

pos_res = (-b + sqrt(b**2 - 4*a*c))/(2*a)
neg_res = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f'The roots are {pos_res} and {neg_res}.')
