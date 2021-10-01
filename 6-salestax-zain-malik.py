# 6) Sales Tax by Zain Malik
# print statements that state purpose of this program
print("")
print("This program will compute the state and county sales tax of a purchase.")
print("")

# set variables
price = input("What is the price of the item you purchased in US Dollars? ")
state = 0.04
county = 0.02
statetax = state * int(price)
countytax = county * int(price)
total = statetax + countytax
amount = total + int(price)

# print statements that shows results
print("")
print("The price of your purchase is $", price)
print("The amount of state sales tax you have to pay is $", statetax)
print("The amount of county sales tax you have to pay is $", countytax)
print("The amount of total sales taxes you have to pay is $", total)
print("The total amount of money you have to pay is $", amount)