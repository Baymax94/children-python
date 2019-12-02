fruits = ['apple', 'banana', 'grape', 'orange']
for fruit in fruits:
    if 'e' not in fruit:
        index = fruits.index(fruit)
        print(fruit, index)
