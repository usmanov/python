# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
paying = random.choice(names)
# TODO-1 Generate random name from the list
print(f"{paying} is going to pay for the meal today")