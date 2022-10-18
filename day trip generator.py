import random
print("")
destination_choice = ["Disney World", "New Zealand", "The Savannah"]
destination = (random.choice(destination_choice))
restaurant_choice = ["local cuisine", "pizza", "American fare"]
restaurant = (random.choice(restaurant_choice))
mode_of_transportation = ["cruise liner", "airplane", "Amtrack"]
transportation = (random.choice(mode_of_transportation))
entertainment = ["deep sea fishing", "hiking", "safari tour"]
fun = (random.choice(entertainment))

create_my_dream_vacation = {
    "destination": destination,
    "restaurant": restaurant,
    "transportation": transportation,
    "fun": fun}

print(create_my_dream_vacation)    
print("")

destination_approval = input("Do you like your destination option? \n")
while destination_approval != "yes":
    new_destination = (random.choice(destination_choice))
    print(new_destination)
    destination_approval = input("Do you like your new destination option? \n")
    if destination_approval == "yes":
        create_my_dream_vacation["destination"] = new_destination
print("Great choice!\n")
restaurant_approval = input("Do you like your restaurant option? \n")
while restaurant_approval != "yes":
    new_restaurant = (random.choice(restaurant_choice))
    print(new_restaurant)
    restaurant_approval = input("Do you like your new retaurant option? \n")
    if restaurant_approval == "yes":
        create_my_dream_vacation["restaurant"] = new_restaurant
print("Great choice!\n")
transportation_approval = input("Do you like your travel option? \n")
while transportation_approval != "yes":
    new_transportation = (random.choice(mode_of_transportation))
    print(new_transportation)
    transportation_approval = input("Do you like your new travel option? \n")
    if transportation_approval == "yes":
        create_my_dream_vacation["transportation"] = new_transportation
print("Great choice!\n")
fun_approval = input("Do you like your entertainment option? \n")
while fun_approval != "yes":
    new_entertainment = (random.choice(entertainment))
    print(new_entertainment)
    fun_approval = input("Do you like your new entertainment option? \n")
    if fun == "yes":
        create_my_dream_vacation["destination"] = entertainment
print("Great choice!\n")
print(f"Your dream vacation is {create_my_dream_vacation}. We'll see you soon!")
