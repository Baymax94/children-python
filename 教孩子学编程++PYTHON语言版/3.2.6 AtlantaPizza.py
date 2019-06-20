#AtlantaPizza.py - a simple pizza cost calculator
#eval()函数
#Ask the person how many pizzas they want, get the number with eval()
number_of_pizzas = eval(input("How many pizzas do you want? \n"))

#Ask for the menu cost of each pizza
cost_per_pizza = eval(input("How much does each pizza costs? \n"))

#Calculate the total cost of the pizzas as our subtotal
subtotal = number_of_pizzas * cost_per_pizza

#Calculate the sales tax owed, at 8% of the subtotal
tax_rate = 0.08 #Store 8% as the decimal value 0.08
sales_tax = subtotal * tax_rate

#Add the sales tax to the subtotal for the final total
total = subtotal + sales_tax

#Show the user the total amount due, including tax
print("The total cost is $",total)
print("This includes $",subtotal,"for the pizza and")
print("$",sales_tax,"in sales tax.")