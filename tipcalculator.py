print(
"""
Tip Calculator

Easily Calculates Your Tip

Enter the amount of your bill. Only enter dollar amount, not cents.
"""
)

# Store the user's cost of bill into the variable of the bill

bill = input('How much was your bill?')
print("%.2f" % bill)

#Change the user's answer to an integer and assign it
# to the variable meal

#Store the value of 10% variable meal into the variable ten
ten = float(bill * .10)

#Store the value of 15% variable meal into the variable fifteen
fifteen = float(bill * .15)

#Store the value of the 20% variable meal into the variable twenty
twenty = float(bill * .20)

#Show the user their calculated tip
print("For 10%, your tip is", ten)


print("For 15%, your tip is", fifteen)


print("For 20%, your tip is", twenty)
