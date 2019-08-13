from fractions import Fraction
# eval函数将输入的字符串当成有效的表达式来求值并返回计算结果
number = eval(input("How many books do you want?"))
cost = eval(input("How much does each book cost?"))
total = number*cost
discount = Fraction(3/4)
finally_total = total*discount
total_finally_total = total - finally_total
print("The cost of these books is {}".format(total))
print("The discount of the activity is {}".format(discount))
print("The reality cost of these books is {}".format(finally_total))
print("The activity has saved money: {}".format(total_finally_total))