# 7) Miles-Per-Gallon by Zain Malik
# print statements that state purpose of this program
print("")
print("This program will determine a car's miles-per-gallon.")
print("")

# set variables
miles = input("How many miles has the car driven? ")
gas = input("How many gallons of gas have been used? ")
mpg = int(miles) / int(gas)

# print statement that shows result
print("The car has driven", mpg, "miles per gallon")