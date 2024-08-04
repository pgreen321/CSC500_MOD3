# PART 1: Create a program that calculates the total amount of a meal purchased at a restaurant

# Tell user this program will calculate the total cost of a meal including food, 18% tip and 7% tax
print('This program will calculate the total cost of a meal, including the cost of the food, an 18% tip and 7% tax')

# Ask user to enter the charge for the food
print()
food_price = float(input('Enter the cost of the food:\n'))

# Calculate the amounts with 18% tip and 7% sales tax
tip_amount = food_price * 0.18
tax_amount = food_price * .07
total_cost = food_price + tip_amount + tax_amount

# Display each of these amounts and the total Price
print()
print('The cost of your food was: ${:.2f}'.format(food_price))
print('An 18% tip is: ${:.2f}'.format(tip_amount))
print('7% Tax on the food is: ${:.2f}'.format(tax_amount))
print('The total cost of the food plus tip and tax is: ${:.2f}'.format(total_cost))


# Part 2: Write a python program to solve the problem of 24 hour time
print()
print('This program will calculate the time an alarm will go off in 24-hour time')
# Ask the user for the time now in hours on a 24-hour clock & how many hours to wait for the alarm
print()
current_time = int(input('What is the current time in hours in 24 hour time? (Example: If it is 1pm, enter 13)\n'))
wait_hours = int(input('How many hours from now should an alarm go off?\n'))

# Calculate the future time (the remainder of the sum of the two times divided by 24 hours
future_time = (current_time + wait_hours) % 24

# Output what the time will be on a 24-hour clock when the alarm goes off
print()
print('The current time is {}:00 hours (on a 24-hour clock)'.format(current_time))
print('The number of hours to wait before your alarm goes off is {}'.format(wait_hours))
print('The time will be {}:00 hours when your alarm goes off (on a 24-hour clock)'.format(future_time))
