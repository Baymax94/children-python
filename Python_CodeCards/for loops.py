# for loops
colours = ("Red", "Orange", "Yellow")
for colour in colours:
    print(colour, end="  ")

# range()
'''
rang([start], [up to but not including], [steps])
starts from zero if omitted    required    only used with both other arguments
'''
for i in range(6):
    print(i, end="  ")

for i in range(2, 6):
    print(i, end="  ")

for i in range(2, 6, 2):
    print(i, end="  ")

colours = ("Red", "Orange", "Yellow")
for i in range(1, 2):
    print(i, colours[i])
