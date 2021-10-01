# 9) Stock Transaction Program by Zain Malik
# print statements that state purpose of this program
print("")
print("Joe purchased some stock in Acme Software, Inc and then sold it later")
print("This program will display information regarding his stock transaction.")
print("")

# set variables
# bought stock
shares = 1000
shareprice = 32.87
shareamount = shares * shareprice
percent = 0.02
brokerpayment = shareamount * percent
# sold stock
shareprice2 = 33.92
shareamount2 = shares * shareprice2
brokerpayment2 = shareamount2 * percent
# money left
money = shareamount2 - shareamount - brokerpayment2 - brokerpayment

# print statement that shows result
print("Joe paid $", shareamount, "for the stock.")
print("Joe paid his broker $", brokerpayment, "as commission when he bought the stock.")
print("Joe sold the stock for $", shareamount2,".")
print("Joe paid his broker $", brokerpayment2, "as commission when he sold the stock.")
print("Joe had $", money, "left over after he sold the stock and payed his broker both times.")
print("Joe lost money.")