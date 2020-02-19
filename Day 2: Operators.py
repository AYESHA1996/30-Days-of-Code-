mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())
tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100
totalCost = mealCost + tip + tax
print("The total meal cost is " + str(round(totalCost)) + " dollars.")

#Alternate

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
tip=meal_cost*(tip_percent/100)
tax=meal_cost*(tax_percent/100)
totalCost=meal_cost+tip+tax
print(round(totalCost))
