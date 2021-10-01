# 8) Tip, Tax, and Total by Zain Malik
# print statements that state purpose of this program
print("")
print("This program will determine the total amount of a meal purchased at a restaurant.")
print("")

# set variables
food = input('How much did the food cost in US Dollars? ')
tip = 0.15
tipcost = tip * int(food)
tax = 0.07
salestax = int(food) * tax
total = int(food) + tipcost + salestax

# print statement that shows result
print("The cost of the food was $", food)
print("The tip was $", tipcost)
print("The sales tax was $", salestax)
print("The total amount of your meal is $", total)