# Function to print out the dwarves in a numbered list
def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

# Function to capitalize and add an exclamation point to planeteer calls
def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

# Function to check if any calls are longer than four characters
def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

# Function to find and return the first type of cheese in a list
def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None
