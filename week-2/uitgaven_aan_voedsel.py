# Write your solution here
meals_in_cafeteria = float(input('How many times a week do you eat lunch at the student cafeteria?'))
avg_price = float(input('The price of a typical student lunch?'))
avg_groceries_p_week = float(input('How much money do you spend on groceries in a week?'))

avg_week_exp = meals_in_cafeteria * avg_price + avg_groceries_p_week
avg_day_exp = avg_week_exp / 7

day_display = round(avg_day_exp, 2)
week_display = round(avg_week_exp, 2)

print(f'Daily: {day_display} euros')
print(f'Weekly: {week_display} euros')
