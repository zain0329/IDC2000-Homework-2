# 4) Total Purchase by Zain Malik
# print statements that state purpose of this program
print("")
print("You are purchasing 5 items in a store. ")
print("This program will determine the subtotal of the sale, the amount of sales tax, and the total amount you owe.")
print("")

# set variables
item1 = input("What is the price of the first item in US dollars? ")
item2 = input("What is the price of the second item in US dollars? ")
item3 = input("What is the price of the third item in US dollars? ")
item4 = input("What is the price of the fourth item in US dollars? ")
item5 = input("What is the price of the fifth item in US dollars? ")
subtotal = int(item1) + int(item2) + int(item3) + int(item4) + int(item5)
tax = 0.06
taxval = tax * subtotal
total = subtotal + taxval

# print statements that shows results
print("")
print("Your subtotal is $", subtotal)
print("You need to pay $", taxval, "in sales tax.")
print("The total amount you need to pay is $", total)

