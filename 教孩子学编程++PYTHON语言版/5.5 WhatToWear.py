rainy = input("How's the weather? Is it raining? (y/n)").lower()
#lower():确保输入小写
cold = input("Is it cold outside? (y/n)").lower()
if (rainy == 'y' and cold == 'y'):          # Rainy and cold, yuck!
    print("You'd better wear a raincoat")
elif (rainy == 'y' and cold != 'y'):        # Rainy, but warm
    print("Carry an umbrella with you.")
elif (rainy != 'y' and cold == 'y'):        # Dry, but cold
    print("Put on a jacket, it's cold out!")
elif (rainy != 'y' and cold != 'y'):        # Warm and sunny, yay!
    print("Wear whatever you want, it's beautiful outside!")