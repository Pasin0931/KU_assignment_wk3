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
    """ Display list of exercises.

        :param: None
        :return: None
    """
    exercise_list = list(BURNED_CALORIES_PER_HOUR.keys())
    print(exercise_list)


def ask_personal_info():
    """ Read values of name, gender, age, weight, height and exercise type
            from the user and return them.

        Information on each value:
            name: Name of user
                  When name is returned, captialize the first letter.
            gender: Gender of user: either 'F' for female or 'M' for male.
            age: Age of user in years (int).
            weight: Weight of user in kilograms (float).
            height: Height of user in centimeter (float).
            exercise: Exercise type chosen by the user. One of:
                ['aerobics', 'badminton', 'cycling', 'housework', 'running', 
                'swimming', 'walking'?]
                When exercise is returned, it will be in all lowercases.

        :param: None
        :return: name, gender, age, weight, height and exercise type
        :rtype: tuple(string, string, int, float, float, string)
    """
    # store user's name in name, and check if the input is empty or not.
    while True:
        name = str(input("Enter your name: ")).title()
        if name == "":
            print("Please provide valid name.")
        else: break

    # store user's gender value, make letter into uppercase, and check if the input is either M or F
    while True:
        gender = str(input("Enter your gender (M/F): ")).upper()
        if gender not in ("M", "F"):
            print("Only (M, F) is allowed.")
        else: break

    # store user's age in age, and check if the input is valid or not
    while True:
        try:
            age = int(input("Enter your age: "))
            if type(age) == int:
                break
        except ValueError:
            print("Please provide valid syntax.")

    # store user's weight in weight, and check if the input is valid or not
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            if type(weight) == int or type(weight) == float:
                break
        except ValueError:
            print("Please provide valid syntax.")

    # store user's height in height, and check if the input is valid or not.
    while True:
        try:
            height = float(input("Enter your height (cm): "))
            if type(height) == int or type(height) == float:
                break
        except ValueError:
            print("Please provide valid syntax.")

    # display every exercises avalible
    display_exercise_list()
    
    # get user's exercise choices, check if is in the dict or not, or input is empty or not
    while True:
        try:
            exercise = str(input("How will you exercise? ")).lower()
            if exercise not in BURNED_CALORIES_PER_HOUR.keys() or exercise == "":
                print("Please provide avalible exercise.")
            else:
                break
        except ValueError:
            print("Please provide valid syntax.")

    # return user inputed variables 
    return name, gender, age, weight, height, exercise


def compute_bmr(weight, height, gender='M', age=30):
    """ Using the parameters, compute and return a Basal Metabolic Rate (BMR),
            based on user parameters.

        The BMR is calculated using the Harris-Benedict equations:
            Men: BMR = 88.362 + (13.397 x weight in kg) + 
                       (4.799 x height in cm) - (5.677 x age in years)
            Women: BMR = 447.593 + (9.247 x weight in kg) + 
                        (3.098 x height in cm) - (4.330 x age in years)

        :param gender: Gender of user, either 'F' for female or 'M' for male.
        :type gender: str
        :param age: Age of user in years.
        :type age: int
        :param weight: Weight of user in kilograms.
        :type weight: float
        :param height: Height of user in centimeters.
        :type height: float
        :return: BMR value computed based on the provided parameters.
        :rtype: float
        >>> compute_bmr(80, 170, 'M', 30)
        1805.6420000000003
        >>> compute_bmr(55.2, 165, 'F', 22)
        1373.9374
        >>> compute_bmr(52, 180.5, 'M', 45)
        1395.7605
        >>> compute_bmr(75.9, 162, 'F', 55)
        1413.1662999999999
        >>> compute_bmr(55.2, 165, 'F')
        1339.2974
        >>> compute_bmr(55.2, 165)
        1449.4014000000002
    """
    # seperate calculation into male and female section.
    if gender == "M":
        bmr_val = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    
    elif gender == "F":
        bmr_val = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return bmr_val


def compute_tdee(bmr):
    """ Use the BMR to compute and return TDEE (Total Daily Energy Expenditure)  
            for 5 difference active levels.
        The TDEE values are calculated as follows:
            1. Sedentary (little or no exercise): BMR x 1.2
            2. Lightly active (1-3 workouts/week): BMR x 1.375
            3. Moderately active (4-5 workouts/week): BMR x 1.55
            4. Very active (6-7 workouts/week): BMR x 1.725
            5. Extremely active (physical job or training): BMR x 1.9

        TDEE is generally a floating-point value. For simplicity in display, 
            each TDEE value will be rounded up to the nearest integer.

        :param bmr: BMR value
        :type bmr: float
        :return: TDEE values for five activity levels
        :rtype: tuple(int, int, int, int, int)
        >>> compute_tdee(1805.6420000000003)
        (2167, 2483, 2799, 3115, 3431)
        >>> compute_tdee(1373.9374)
        (1649, 1890, 2130, 2371, 2611)
        >>> compute_tdee(1395.7605)
        (1675, 1920, 2164, 2408, 2652)
        >>> compute_tdee(1413.1662999999999)
        (1696, 1944, 2191, 2438, 2686)
    """
    # calculate tdee of sedentary, lightly-active, moderately-active, very-active, extremely-active
    sedentary = bmr * 1.2
    lightly_active = bmr * 1.375
    moderately_active = bmr * 1.55
    very_active = bmr * 1.725
    extremely_active = bmr * 1.9
    
    # round every value to full number and return
    return (math.ceil(sedentary),
            math.ceil(lightly_active),
            math.ceil(moderately_active),
            math.ceil(very_active),
            math.ceil(extremely_active))


def display_food_items(calories_dict, food_type):  
    """ Display food items for a specific food_type.

        The food items are generally the keys from calories_dict 
        Note that calories_dict is one of three dictionaries declared at the 
            begining of program:
            -Keys of these dictionaries are food items.
            -Values of these dictionaries are calorie amounts.

        :param calories_dict: Dictionary containing calories of food items.
        :type num_cells: dict
        :param food_type: Type of food to display; either 'entree', 'dessert', 
                          or 'drink'.
        :type food_type: str
    """
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
    """ Read a food item from user for a specific food_type and specific meal.

        The food item is checked against calories_dict to ensure it exists.
        If the entered food item is invalid (or does not exists in the 
            dictionary), the user is notified and prompt to enter another item.
        This process continues until a valid food item is entered.
        The valid food item will be returned.

        :param calories_dict: Dictionary containing calories of food items.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        :type num_cells: dict
        :param food_type: Type of food to display; either 'entree', 'dessert',
            or 'drink'.
        :type food_type: str
        :param meal_num: Number specifying which meal of the day.
        :type meal_num: int
        :return: A valid food item entered by the user.
        :rtype: str
    """
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
    """ Create and return a string summarizing a meal 
            based on the provided parameters.

        :param meal_num: Number specifying which meal of the day.
        :type meal_num: int
        :param entree: Entree item.
        :type entree: str
        :param entree_cal: Calories of the entree item.
        :type entree_cal: int
        :param dessert: Dessert item.
        :type dessert: str
        :param dessert_cal: Calories of the dessert item.
        :type dessert_cal: int
        :param drink: Drink item.
        :type drink: str
        :param drink_cal: Calories of the drink item.
        :type drink_cal: int
        :param total_cal_sum: Cumulative calories, including this meal.
        :type total_cal_sum: int
        :return: A formatted string summarizing the mealm including items and 
                their calories. 
        :rtype: str
        >>> __summary = acquire_meal_summary(2, 'suki', 345, 'fruit', 80, 'pure matcha', 5, 1860)
        >>> print(__summary)
        <BLANKLINE>
        Meal #2 Summary:
        Entree: suki, 345 kcal.
        Dessert: fruit, 80 kcal.
        Drink: pure matcha, 5 kcal.
        Meal calories: 430 kcal.
        Cumulative calories: 1860 kcal.
        >>> __summary2 = acquire_meal_summary(3, 'pizza', 700, 'ice cream', 260, 'soda', 130, 2330)
        >>> print(__summary2)
        <BLANKLINE>
        Meal #3 Summary:
        Entree: pizza, 700 kcal.
        Dessert: ice cream, 260 kcal.
        Drink: soda, 130 kcal.
        Meal calories: 1090 kcal.
        Cumulative calories: 2330 kcal.
    """
    # return every values that passed into the function in sentences
    return (f"\nMeal #{meal_num} Summary:"
            f"\nEntree: {entree}, {entree_cal} kcal."
            f"\nDessert: {dessert}, {dessert_cal} kcal."
            f"\nDrink: {drink}, {drink_cal} kcal."
            f"\nMeal calories: {entree_cal + dessert_cal + drink_cal} kcal."
            f"\nCumulative calories: {total_cal_sum} kcal.")


def ask_diet_info():  
    """ Prompt the user for the number of meals he eats per day.
        Then, for each meal:
            Ask the user to enter the entree, dessert and drink (via ).
            Display the meal summary (via function acquire_meal_summary).
            Update the cumulative calories.
        Return the cumulative calories for all meals.

        :param: None
        :return: Cumulative calories.
        :rtype: int
    """
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
    """ Compute and return the difference between consumed and needed calories.
        If the difference is zero or negative, return zero.

        :param consumed_calories: Calories consumed from food.
        :type consumed_calories: int
        :param needed_calories: Calories required by the body.
        :type needed_calories: int
        :return: Difference between consumed and needed_calories,
        :           or zero if negative
        :rtype: int
        >>> compute_excess_calories(1860, 1920)
        0
        >>> compute_excess_calories(1920, 1860)
        60
        >>> compute_excess_calories(1650, 2131)
        0
        >>> compute_excess_calories(2790, 2371)
        419
    """
    # calculate if there's excess calories
    kcal = needed_calories - consumed_calories
    
    # if the result is above 0 means there are no excess calories
    if kcal >= 0:
        return 0
    elif kcal < 0:
        return kcal * -1  


def compute_exercise_duration(_exercise, _excess_cal):
    """ Compute the required exercise duration in FULL minutes, 
            based on the given exercise type and the excess calories.
        The duration is rounded up to the nearest full minute.

        :param _exercise: Exercise type chosen by the user.
        :type _exercise: str
        :param _excess_cal: Excess calories to burn.
        :type _excess_cal: int
        :return: Exercise duration in full minutes.
        :rtype: int
        >>> compute_exercise_duration('cycling', 250)
        27
        >>> compute_exercise_duration('walking', 500)
        131
        >>> compute_exercise_duration('housework', 300)
        84
    """
    # turn 1 hour into 60 minutes
    full_minute = 60
    
    # check if _exercise is in NURNED_CALORIES_PER HOUR or not
    if _exercise in BURNED_CALORIES_PER_HOUR:
        # loop until find index where exercise is present
        for i in BURNED_CALORIES_PER_HOUR:
            if i == _exercise:
                # pass calories of BURNED_CALORIES_PER_HOUR of that exercise and compute
                kcal = BURNED_CALORIES_PER_HOUR[i]
                result = (_excess_cal * full_minute) / kcal
    
    # floor result value and return
    return math.ceil(result)


def acquire_exercise_summary(_exercise, _excess_cal):
    """ Create and return a string summarizing the user's exercise requirement.

        The summary indicates whether the user needs to exercise.  
            - If excess calories are zero, no exercise is needed.  
            - Otherwise, the summary shows the exercise type and duration 
                in full minutes, based on the user's choice.

        :param _exercise: Exercise type chosen by the user.
        :type _exercise: str
        :param _excessive_cal: Excess calories
        :type _excessive_cal: int
        :return: Exercise summary string
        :rtype: str
        >>> __summary = acquire_exercise_summary('cycling', 250)
        >>> print(__summary)
        You consumed 250 kcal in excess and need to do cycling for 27 minutes.
        >>> __summary2 = acquire_exercise_summary('walking', 0)
        >>> print(__summary2)
        You do not need to remove excess calories.
    """
    # check if there's an excess calories
    if _excess_cal == 0:
        return f"You do not need to remove excess calories."
    else:
        return (f"You consumed {_excess_cal} kcal in excess and need to do "
                f"{_exercise} for {compute_exercise_duration(_exercise, _excess_cal)} minutes.")


def display_summary(_exercise, total_cal_sum, activity_level, tdee):
    """ Display whether the user needs to exercise based on consumed calories
            and the TDEE for different activity levels.

        Activity levels indicates how much physical activity the user do in
            a day. The value ranges from 1 to 5:
            1 = little or no exercise
            5 = extremely active
        See the function compute_tdee() for more details.

        :param _exercise: Exercise type chosen by the user.
        :type _exercise: str
        :param total_cal_sum: Cumulative calories.
        :type total_cal_sum: int
        :param active_level: Activity level (1-5).
        :type active_level: int
        :return: 
        :rtype: str
        >>> __summary = display_summary('cycling', 2130, 1, 1649)
        >>> print(__summary)
        <BLANKLINE>
        If you are sedentary (little or no exercise), your suggested daily calories are 1649 kcal.
        You consumed 481 kcal in excess and need to do cycling for 52 minutes.
        >>> __summary2 = display_summary('running', 2130, 2, 1890)
        >>> print(__summary2)
        <BLANKLINE>
        If you are lightly active (1-3 workouts/week), your suggested daily calories are 1890 kcal.
        You consumed 240 kcal in excess and need to do running for 27 minutes.
    """
    # pass down excess calories value into excess
    excess = compute_excess_calories(total_cal_sum, tdee)

    # pass down return value of acquire_exercise_summary into exercise_msg
    # if no excess calories will be "You do not need to remove excess calories."
    exercise_msg = acquire_exercise_summary(_exercise, excess)
    
    # return activity level from function's parameter
    if activity_level == 1:
        return (f'\nIf you are sedentary (little or no exercise),'
                f'your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}')
    
    elif activity_level == 2:
        return (f'\nIf you are lightly active (1-3 workouts/week), '
                f'your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}')
    
    elif activity_level == 3:
        return (f'\nIf you are moderately active (4-5 workouts/week), '
                f'your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}')
    
    elif activity_level == 4:
        return (f'\nIf you are very active (6-7 workouts/week), '
                f'your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}')
    
    elif activity_level == 5:
        return (f'\nIf you are extremely active (physical job or training), '
                f'your suggested daily calories are {tdee} kcal.\n'
                f'{exercise_msg}')


# Main part

# store values return from ask_personal_info into these variables
name, gender, age, weight, height, exercise = ask_personal_info()

# Fill in the code before ask_diet_info() here
day_calories = ask_diet_info()
# Fill in the code after here

# get bmr value and pass into bmr
bmr = compute_bmr(weight, height, gender, age)
# get tdee value and pass into tdee_values
tdee_values = compute_tdee(bmr)

print("===============")
print(f"Overall Summary:")
print(f"{name}, you consumed {day_calories} kcal.")

# loop to display each level from level 1 to 5
for level in range(1, 6):
    print(display_summary(exercise, day_calories, level, tdee_values[level-1]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()