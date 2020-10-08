
cars = ['audi','bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Boolean Expressions:
# True and False - MUST BE UPPERCASE T and F

car = "bmw" # assigns bmw to variable car
car  == "bmw" # Comparison of car and bmw
# Testing the string is case sensitive (above would be false if B was capital)

# != checks for inequality

# Can use and/or to check multiple conditions (slide 8 example)

# You can check if a value is in a list
toppings = ['mushrooms', 'onions', 'pinapple']
if 'mushrooms' in toppings: # use 'not in' instead here to check if something is not in a list
    print("Yes, it is in the list.")


age = 20
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")


requested_toppings = ['Pepperoni']
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'extra cheeSe', 'olives', 'pineapple', 'pepperoni', 'green peppers']
requested_toppings = ['mushrooms', 'french fries', 'extRa cheese']


# To fix the case sensitive problem
new_list = []
for available_topping in available_toppings:
    new_list.append(available_topping.lower())

for requested_topping in requested_toppings:
    if requested_topping.lower() in new_list:
        print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")




