fruits = {'apple':5, 'banana':8, 'grape':2, 'orange':9}
temp = []

for fruit in fruits.keys():
    if 'e' not in fruit:
        temp.append(fruit)
        
for key in temp:
    del fruits[key]

print(fruits)
