FOOD_DATA = {
    'entrees': {
        'porridge': 200,
        'grilled pork': 320,
        'pork bun': 200,
        'cereal': 250,
        'egg and sausage': 550,
        'basil pork': 580,
        'chicken rice': 590,
        'bbq pork rice': 540,
        'garlic pork rice': 520,
        'rice and curry': 480,
        'noodle soup': 270,
        'suki': 345,
        'rat na noodle': 400,
        'fried noodle': 620,
        'fried rice': 550,
        'somtam': 110,
        'yam woon sen': 170,
        'chicken salad': 120,
        'instant noodle': 250,
        'spaghetti': 430,
        'ham sandwich': 290,
        'burger and fries': 620,
        'pizza': 700,
        'pork steak': 540,
        'fried chicken': 710,
    },
    'desserts': {
        'fruit': 80,
        'mango sticky rice': 170,
        'potato chips': 180,
        'ice cream': 260,
        'cookies': 240,
        'brownie': 160,
        'donut': 180,
        'croissant': 270,
        'cake': 370,
        'none': 0,
    },
    'drinks': {
        'milk': 160,
        'soy_milk': 100,
        'juice': 110,
        'soda': 130,
        'black coffee': 15,
        'iced capucino': 150,
        'matcha': 5,
        'matcha latte': 130,
        'smoothie': 115,
        'water': 0,
    }
}

EXERCISE_DATA = {
    'aerobics': 600,
    'badminton': 315,
    'cycling': 560,
    'housework': 215,
    'running': 550,
    'swimming': 420,
    'walking': 230
}

# this_exercise = list(EXERCISE_DATA.keys())[2]
# this_data = FOOD_DATA['entrees']['porridge']
# print(this_data)

exercise_keys = list(EXERCISE_DATA.keys())
exercise = exercise_keys[1]
print(exercise)