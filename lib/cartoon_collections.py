def roll_call_dwarves(dwarves):
    for i, name in enumerate(dwarves, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(planeteer_calls):
    capitalized_calls = [call.capitalize() + "!" for call in planeteer_calls]
    return capitalized_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for string in strings:
        if string in cheese_types:
            return string
    return None

