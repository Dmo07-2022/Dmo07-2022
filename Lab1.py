# Program Name: Lab1.py
# Course: IT1114/Section W01
# Student Name: Daryl Maurice
# Assignment Number: Lab#1
# Due Date: 08/28/2022
# Purpose: This program will help the user calculate 
# the amount and cost of purchasing flooring.
# Referenced Module 3 Output Formatting lecture video to assist with escape characters,
# rounding functions, and format strings.

# Variable declaration.
# Ask the user to enter the room length, width, and cost per square foot.
length = float(input("\nPlease enter the room length: "))
width = float(input("Please enter the room width: "))
cost_sqft = float(input("Please enter the cost of the flooring per square foot: "))

# Calculate the total square feet, flooring cost, tax, and total amount due.
total_sqr_feet = length * width
flooringcost = cost_sqft * total_sqr_feet
tax = flooringcost * .07
total_amt_due = flooringcost + tax

# Print out the total square feet required, cost per sq.ft, applicable tax, and total cost.
print("\nFlooring Cost")
print("Square feet: ", total_sqr_feet)
print("Flooring (", cost_sqft, "/sq.ft)\t", "$", f"{flooringcost}", sep="")
print("Tax (7%)\t\t\t\t", " $", round(tax, 2), sep="")
print("Total\t\t\t\t\t", "$", f"{total_amt_due:0.2f}", sep="")




