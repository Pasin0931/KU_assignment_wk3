import math


ENTREE_CALORIES = {'porridge': 200,
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
                   }


DESSERT_CALORIES = {'fruit': 80,
                    'mango sticky rice': 170,
                    'potato chips': 180,
                    'ice cream': 260,
                    'cookies': 240,
                    'brownie': 160,
                    'donut': 180,
                    'croissant': 270,
                    'cake': 370,
                    'none': 0
                    }


DRINK_CALORIES = {'milk': 160,
                  'soy_milk': 100,
                  'juice': 110,
                  'soda': 130,
                  'black coffee': 15,
                  'iced capucino': 150,
                  'pure matcha': 5,
                  'matcha latte': 130,
                  'smoothie': 115,
                  'water': 0
                  }


BURNED_CALORIES_PER_HOUR = {'aerobics': 600,
                            'badminton': 315,
                            'cycling': 560,
                            'housework': 215,
                            'running': 550,
                            'swimming': 420,
                            'walking': 230,
                            }


def display_exercise_list():  

    exercise_list = list(BURNED_CALORIES_PER_HOUR.keys())
    print(exercise_list)
    pass


def ask_personal_info():

    name = str(input("Enter your name: ")).title()
    gender = str(input("Enter your gender (M/F): ")).upper()
    if gender not in ("M", "F"):
        gender = "M"
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    
    display_exercise_list()
    
    exercise = str(input("How will you exercise? ")).lower()
    
    return name, gender, age, weight, height, exercise
    pass


def compute_bmr(weight, height, gender='M', age=30):
    
    if gender == "M":
        bmr_val = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    
    elif gender == "F":
        bmr_val = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return bmr_val
    pass


def compute_tdee(bmr):
    
    sedentary = bmr * 1.2
    lightly_active = bmr * 1.375
    moderately_active = bmr * 1.55
    very_active = bmr * 1.725
    extremely_active = bmr * 1.9
    
    return math.ceil(sedentary), math.ceil(lightly_active), math.ceil(moderately_active), math.ceil(very_active), math.ceil(extremely_active)
    pass


def display_food_items(calories_dict, food_type):  

    # find the length of longest food name
    max_item_len = max([len(key) for key in calories_dict])

    # to display 5 food items per line
    num_items_per_line = 5
    # max_item_len+5: +5 to accommodate:
    # 2-digit food number, a dot, and a space in front of of food item and '|'
    # after food item
    print('-'*(num_items_per_line*(max_item_len+5)))  # draw a line of '-'
    print(food_type.capitalize() + ' Choices:')
    print('-'*(num_items_per_line*(max_item_len+5)))  # draw a line of '-'
    item_list = list(calories_dict.keys())
    for i in range(len(item_list)):
        print(f'{i+1:>2}. {item_list[i]:<{max_item_len}}|', end='')
        if (i+1) % num_items_per_line == 0:
            print()
    print('-' * (num_items_per_line*(max_item_len+5)))  # draw a line of '-'


def read_item(calories_dict, food_type, meal_num):
    display_food_items(calories_dict, food_type)
    item_list = list(calories_dict.keys())
    while True:
        item = input(f'For meal #{meal_num}, enter ' + food_type + ': ')
        item = item.lower()
        if item in item_list:
            break
        else:
            print('You entered invalid ' + food_type + '. '
                  'Please choose again.')
    return item


def acquire_meal_summary(meal_num, entree, entree_cal, dessert, dessert_cal,
                         drink, drink_cal, total_cal_sum):
    
    return f"Meal#{meal_num} Summary\nEntree:{entree}, {entree_cal} kcal.\nDessert: {dessert}, {dessert_cal} kcal.\nDrink: {drink}, {drink_cal} kcal.\nMeal calories: {entree_cal + dessert_cal + drink_cal}\nCumulative calories: {total_cal_sum}."
    pass


def ask_diet_info():  

    print('Please provide your diet information:')
    num_meals = int(input("How many meals do you eat per day: "))
    # total_cal_sum stores cumulative calories
    total_cal_sum = 0
    for i in range(num_meals):
        # read entree, dessert, and drink item and get its calories
        entree = read_item(ENTREE_CALORIES, 'entree', i+1)
        dessert = read_item(DESSERT_CALORIES, 'dessert', i+1)
        drink = read_item(DRINK_CALORIES, 'drink', i+1)

        # get calories of entree, dessert and drink items
        entree_cal = ENTREE_CALORIES[entree]
        dessert_cal = DESSERT_CALORIES[dessert]
        drink_cal = DRINK_CALORIES[drink]

        # update total calories
        total_cal_sum += entree_cal + dessert_cal + drink_cal

        # display meal summary
        summary = acquire_meal_summary(i+1, entree, entree_cal, 
                                       dessert, dessert_cal, 
                                       drink, drink_cal, total_cal_sum)
        print(summary)

    return total_cal_sum


def compute_excess_calories(consumed_calories, needed_calories):
    
    kcal = needed_calories - consumed_calories
    
    if kcal >= 0:
        return 0
    elif kcal < 0:
        return kcal * -1  
    
    pass


def compute_exercise_duration(_exercise, _excess_cal):
    
    full_minute = 60
    
    if _exercise in BURNED_CALORIES_PER_HOUR:
        for i in BURNED_CALORIES_PER_HOUR:
            if i == _exercise:
                kcal = BURNED_CALORIES_PER_HOUR[i]
                result = (_excess_cal * full_minute) / kcal
    
    return math.ceil(result)
    pass


def acquire_exercise_summary(_exercise, _excess_cal):
    
    if _excess_cal == 0:
        return f"You do not need to remove excess calories."
    else:
        return f"You consumed {_excess_cal} kcal in excess and need to do {_exercise} for {compute_exercise_duration(_exercise, _excess_cal)} minutes."
    pass


def display_summary(_exercise, total_cal_sum, activity_level, tdee):

    excess = compute_excess_calories(total_cal_sum, tdee)
    exercise_msg = acquire_exercise_summary(_exercise, excess)
    
    if activity_level == 1:
        return (f'If you are sedentary (little or no exercise), your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}\n')
    elif activity_level == 2:
        return (f'If you are lightly active (1-3 workouts/week), your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}\n')
    elif activity_level == 3:
        return (f'If you are moderately active (4-5 workouts/week), your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}\n')
    elif activity_level == 4:
        return (f'If you are very active (6-7 workouts/week), your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}\n')
    elif activity_level == 5:
        return (f'If you are extremely active (physical job or training), your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}')
    pass


# Main part

name, gender, age, weight, height, exercise = ask_personal_info()

# Fill in the code before ask_diet_info() here
day_calories = ask_diet_info()
# Fill in the code after here

bmr = compute_bmr(weight, height, gender, age)
tdee_values = compute_tdee(bmr)

print("===============")
print(f"Overall Summary:")
print(f"{name}, you consumed {day_calories} kcal.\n")

for level in range(1, 6):
    print(display_summary(exercise, day_calories, level, tdee_values[level-1]))

