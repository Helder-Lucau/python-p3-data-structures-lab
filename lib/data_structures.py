spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food_name["name"] for food_name in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [spiciest_food for spiciest_food in spicy_foods if spiciest_food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_cuisine in spicy_foods:
        if spicy_cuisine["cuisine"] == cuisine:
            return spicy_cuisine
    # return [cuisine_name for cuisine_name in spicy_foods if cuisine_name["cuisine"] == cuisine]

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    average_level = sum([level["heat_level"] for level in spicy_foods])/len(spicy_foods)
    return average_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
