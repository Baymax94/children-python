driving_age = eval(input("What is the legal driving age where you live? \n"))
your_age = eval(input("How old are you? "))
if your_age >= driving_age:
    print("You're old enough to drive!")
if your_age < driving_age:
    print("Sorry, you can drive in ",driving_age - your_age," years.")