"""
Calorie and Exercise Tracker Program.

This program allows users to track their meals and exercises,
calculate TDEE, and monitor daily and overall calorie balance.
"""

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


def format_exercise_data(data):
    """
    Format exercise data for display in a two-column table.

    Args:
        data (dict): Exercise data to format
    """
    list_data = list(data)

    first_line = list_data[0:-1:2]
    first_line.append(list_data[-1])

    second_line = list_data[1:-1:2]

    count = 1
    for i in range(0, len(first_line)):
        first_line[i] = f"{count}. {first_line[i]}"
        count += 2

    count = 2
    for i in range(0, len(second_line)):
        second_line[i] = f"{count}. {second_line[i]}"
        count += 2

    print(line_long_up)

    for i in first_line:
        print(f"|  {i:<13}", end="")

    print("│               │", end="")
    print()

    for i in second_line:
        print(f"|  {i:<13}", end="")

    spaces = 15 * " "
    print(f"│{spaces}│{spaces}|")
    print(line_long_down)


def format_entree_data(data):
    """
    Format entree data for display in a five-column table.

    Args:
        data (list): Entree data to format
    """
    line_1 = data[0:-1:5]
    line_2 = data[1:-1:5]
    line_3 = data[2:-1:5]
    line_4 = data[3:-1:5]
    line_5 = data[4:-1:5]
    line_5.append(data[-1])

    count = 1
    for i in range(0, len(line_1)):
        line_1[i] = f"{count}. {line_1[i]}"
        count += 5

    count = 2
    for i in range(0, len(line_2)):
        line_2[i] = f"{count}. {line_2[i]}"
        count += 5

    count = 3
    for i in range(0, len(line_3)):
        line_3[i] = f"{count}. {line_3[i]}"
        count += 5

    count = 4
    for i in range(0, len(line_4)):
        line_4[i] = f"{count}. {line_4[i]}"
        count += 5

    count = 5
    for i in range(0, len(line_5)):
        line_5[i] = f"{count}. {line_5[i]}"
        count += 5

    print(line_long_up)

    for i in line_1:
        print(f"|  {i:<21}", end="")
    print("|")

    for i in line_2:
        print(f"|  {i:<21}", end="")
    print("|")

    for i in line_3:
        print(f"|  {i:<21}", end="")
    print("|")

    for i in line_4:
        print(f"|  {i:<21}", end="")
    print("|")

    for i in line_5:
        print(f"|  {i:<21}", end="")
    print("|")

    print(line_long_down)


def format_dessert_drink_data(data):
    """
    Format dessert or drink data for display in a two-column table.

    Args:
        data (list): Dessert or drink data to format
    """
    line_1 = data[0:-1:2]
    line_2 = data[1:-1:2]
    line_2.append(data[-1])

    count = 1
    for i in range(0, len(line_1)):
        line_1[i] = f"{count}. {line_1[i]}"
        count += 2

    count = 2
    for i in range(0, len(line_2)):
        line_2[i] = f"{count}. {line_2[i]}"
        count += 2

    print(line_long_up)

    for i in line_1:
        print(f"|  {i:<21}", end="")
    print("|")

    for i in line_2:
        print(f"|  {i:<21}", end="")
    print("|")

    print(line_long_down)


def ask_usr():
    """
    Prompt user for profile information.

    Returns:
        tuple: (name, gender, age, weight, height)
    """
    print("--- Setting up your profile ---")

    while True:
        name = input("Enter your name: ")
        if name == "":
            print(invalid)
        else:
            break

    while True:
        gender = input("Enter your gender (M/F): ").upper()
        if gender == "M" or gender == "F":
            break
        else:
            print(invalid)

    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                break
            else:
                print(invalid)
        except ValueError:
            print(invalid)

    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            if weight > 0:
                break
            else:
                print("Weight must be positive.")
        except ValueError:
            print(invalid)

    while True:
        try:
            height = float(input("Enter your height (cm): "))
            if height > 0:
                print()
                break
            else:
                print("Height must be positive.")
        except ValueError:
            print(invalid)

    return name, gender, age, weight, height


def ask_activity_level(username, gender, w, h, age):
    """
    Prompt user for activity level and calculate TDEE.

    Args:
        username (str): User's name
        gender (str): User's gender
        w (float): User's weight
        h (float): User's height
        age (int): User's age

    Returns:
        tuple: (activity_level, tdee)
    """
    while True:
        print("--- Activity Level ---")
        print("1. Sedentary (little or no exercise)\n"
              "2. Lightly active (1-3 workouts/week)\n"
              "3. Moderately active (4-5 workouts/week)\n"
              "4. Very active (6-7 workouts/week)\n"
              "5. Extremely active (physical job or training)")

        try:
            activity_level = int(input("Choose your activity level (1-5): "))
            if 1 <= activity_level <= 5:
                break
            else:
                print("Please enter a number between 1-5.")
        except ValueError:
            print(invalid)

    if activity_level == 1:
        activity_factor = 1.2
    elif activity_level == 2:
        activity_factor = 1.375
    elif activity_level == 3:
        activity_factor = 1.55
    elif activity_level == 4:
        activity_factor = 1.725
    elif activity_level == 5:
        activity_factor = 1.9

    if gender == "M":
        BMR = 88.362 + (13.397 * w) + (4.799 * h) - (5.677 * age)
    elif gender == "F":
        BMR = 447.593 + (9.247 * w) + (3.098 * h) - (4.330 * age)

    tdee = BMR * activity_factor

    print(f"\nProfile created for {username}. Your TDEE is {tdee:.0f} kcal.\n")
    return activity_level, tdee


def main_page():
    """
    Display main menu and get user choice.

    Returns:
        int: User's menu choice
    """
    while True:
        print("--- Main Menu ---")
        print("1. Add Meals\n"
              "2. Add Exercise\n"
              "3. Remove an Entry\n"
              "4. Show Summary for a Day\n"
              "5. Show Full History\n"
              "6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice > 0 and choice < 7:
                break
            else:
                print("Invalid choice, please try again.\n")
        except ValueError:
            print()
            print(invalid)

    return choice


def add_meal():
    """
    Add meal entries to the database.

    Returns:
        tuple: (year, month, day, meal_data)
    """
    print("--- Adding Your Meals ---")
    while True:
        try:
            ymd = input("Enter the date (YYYY-MM-DD): ").split("-")

            year, month, day = map(int, ymd)

            if year > 0 and 1 <= month <= 12 and 1 <= day <= 31:
                try:
                    datetime.date(year, month, day)
                    break
                except ValueError:
                    print("Invalid date format.")
            else:
                print("Invalid date format.")

        except ValueError:
            print(invalid)

    while True:
        try:
            meal_amount = int(input("How many more meals to add? "))
            if meal_amount <= 0:
                print('Invalid number.')
            else:
                break
        except ValueError:
            print(invalid)

    overall_datas = []

    for meal_num in range(1, meal_amount + 1):
        print(f"\n--- Meal #{meal_num} ---\n")

        print("Entree Choices:")
        format_entree_data(entree_keys)
        while True:
            try:
                entree_choice = int(input("Choose an Entree by number (1-25): "))
                if entree_choice > 0 and entree_choice < 26:
                    selected_meal = entree_keys[entree_choice - 1]
                    selected_meal_kcal = FOOD_DATA["entrees"][selected_meal]
                    break
                else:
                    print("Invalid number.")
            except ValueError:
                print(invalid)

        print("\nDessert Choices:")
        format_dessert_drink_data(dessert_keys)
        while True:
            try:
                dessert_choice = int(input("Choose a Dessert by number (1-10): "))
                if dessert_choice > 0 and dessert_choice < 11:
                    selected_dessert = dessert_keys[dessert_choice - 1]
                    selected_dessert_kcal = FOOD_DATA["desserts"][selected_dessert]
                    break
                else:
                    print("Invalid number.")
            except ValueError:
                print(invalid)

        print("\nDrink Choices:")
        format_dessert_drink_data(drink_keys)
        while True:
            try:
                drink_choice = int(input("Choose a Drink by number (1-10): "))
                if drink_choice > 0 and drink_choice < 11:
                    selected_drink = drink_keys[drink_choice - 1]
                    selected_drink_kcal = FOOD_DATA['drinks'][selected_drink]
                    break
                else:
                    print("Invalid number.")
            except ValueError:
                print(invalid)

        overall_datas.append({selected_meal: selected_meal_kcal})
        overall_datas.append({selected_dessert: selected_dessert_kcal})
        overall_datas.append({selected_drink: selected_drink_kcal})

    print("\nMeals added successfully!\n")
    return year, month, day, overall_datas


def add_exercise():
    """
    Add exercise entry to the database.

    Returns:
        tuple: (year, month, day, exercise_name, kcal_burn_per_hour, kcal_burned, dict_form)
    """
    print("--- Adding Your Exercise ---")
    while True:
        try:
            ymd = input("Enter the date (YYYY-MM-DD): ").split("-")

            year, month, day = map(int, ymd)

            if year > 0 and 1 <= month <= 12 and 1 <= day <= 31:
                try:
                    datetime.date(year, month, day)
                    break
                except ValueError:
                    print("Please enter a proper date.")
            else:
                print("Please enter a proper date.")

        except ValueError:
            print(invalid)

    print("\nExercise Choices:")
    format_exercise_data(EXERCISE_DATA)
    while True:
        try:
            exercise_choice = int(input("Choose an Exercise by number (1-7): "))
            if exercise_choice > 0 and exercise_choice < 8:
                this_exercise = exercise_keys[exercise_choice - 1]
                burn_per_hour = EXERCISE_DATA[this_exercise]
                break
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid number.")

    while True:
        try:
            exercise_duration = float(input("Enter duration for running in minutes: "))
            if exercise_duration > 0:
                burned_kcal = (exercise_duration * burn_per_hour) / 60
                burned_kcal = int(burned_kcal)
                break
            else:
                print("Duration must be positive.")
        except ValueError:
            print(invalid)

    print(f"\nLogged {this_exercise} for {exercise_duration:.1f} minutes, burning {burned_kcal} kcal.\n")

    dict_form = [{this_exercise: burned_kcal}]

    return year, month, day, this_exercise, burn_per_hour, burned_kcal, dict_form


def remove_entry(db):
    """
    Remove a meal or exercise entry from the database.

    Args:
        db (dict): The database to modify
    """
    print("--- Remove an Entry ---")
    date_in = input("Enter the date (YYYY-MM-DD): ").split("-")
    year_ = int(date_in[0])
    month_ = int(date_in[1])
    day_ = int(date_in[2])
    date_in = f"{year_}-{month_}-{day_}"

    if date_in not in db["meals"] and date_in not in db["exercises"]:
        print("No entries for this date.\n")
        return

    while True:
        choice = input("Remove a 'meal' or an 'exercise'? ").strip().lower()
        if choice in ["meal", "exercise"]:
            break
        else:
            print("Please type 'meal' or 'exercise'.")

    if choice == "meal":
        if date_in not in db["meals"] or not db["meals"][date_in]:
            print("No entries for this date.\n")
            return

        meals = db["meals"][date_in]
        entree_all = meals[0:-1:3]
        dessert_all = meals[1:-1:3]
        drink_all = meals[2::3]

        print("\n--- Select Meal to Remove ---")
        for i in range(len(entree_all)):
            entree = list(entree_all[i].keys())[0]
            dessert = list(dessert_all[i].keys())[0]
            drink = list(drink_all[i].keys())[0]
            print(f"{i+1}. Entree: {entree}, Dessert: {dessert}, Drink: {drink}")

        while True:
            try:
                idx = int(input("Enter the number of the meal to remove: "))
                if 1 <= idx <= len(entree_all):
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print(invalid)

        rm_idx = (idx - 1) * 3
        removed = db["meals"][date_in][rm_idx:rm_idx+3]
        del db["meals"][date_in][rm_idx:rm_idx+3]

        print(f"Meal #{idx} has been removed.\n")

    elif choice == "exercise":
        if date_in not in db["exercises"] or not db["exercises"][date_in]:
            print("No exercises for this date.\n")
            return

        exercises = db["exercises"][date_in]
        print("\n--- Select Exercise to Remove ---")
        for i, ex in enumerate(exercises, 1):
            name = list(ex.keys())[0]
            kcal = ex[name]
            print(f"{i}. {name} ({kcal} kcal burned)")

        while True:
            try:
                idx = int(input("Enter the number of the exercise to remove: "))
                if 1 <= idx <= len(exercises):
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Invalid input.")

        removed = db["exercises"][date_in].pop(idx - 1)
        name = list(removed.keys())[0]
        print(f"Exercise '{name}' has been removed.\n")


def show_day_summary(db, tdee):
    """
    Display a summary of meals and exercises for a specific day.

    Args:
        db (dict): The database containing meals and exercises
        tdee (float): User's TDEE value
    """
    line_ = "─" * 69
    line_1 = "─" * 69
    line_2 = "─" * 69

    li_up = f"┌{line_}┐"
    li_mid = f"├{line_1}┤"
    li_down = f"└{line_}┘"

    print("--- Daily Summary ---")
    while True:
        try:
            date_in = input("Enter the date (YYYY-MM-DD): ").split("-")
            date_in[0] = int(date_in[0])
            date_in[1] = int(date_in[1])
            date_in[2] = int(date_in[2])
            pack_ = f"{date_in[0]}-{date_in[1]}-{date_in[2]}"
            if pack_ in db["meals"] or pack_ in db["exercises"]:
                break
            else:
                print("No data found for that date.\n")
                return None
        except ValueError:
            print(invalid)

    meal_day = ""
    exercise_day = ""

    for key, value in db["meals"].items():
        if key == pack_:
            meal_day = value

    for key, value in db["exercises"].items():
        if key == pack_:
            exercise_day = value

    entree_all = meal_day[0:-1:3]
    dessert_all = meal_day[1:-1:3]
    drink_all = meal_day[2::3]

    text_summary = f"Summary for {date_in[0]}-{date_in[1]}-{date_in[2]}"

    print()
    print(li_up)
    print("|" + f"{text_summary}".center(69) + "|")
    print(li_mid)
    print("|" + "Meals Consumed".center(69) + "|")
    print(li_mid)
    print("| " + "Meal #".ljust(9) + "| " + "Entree".ljust(19) + "| " + "Dessert".ljust(19) + "| " + "Drink".ljust(15) + "|")
    print(li_mid)

    total_consumed = 0
    count = 1
    for i in range(len(entree_all)):
        entree = list(entree_all[i].keys())[0]
        dessert = list(dessert_all[i].keys())[0]
        drink = list(drink_all[i].keys())[0]
        entree_kcal = entree_all[i][entree]
        dessert_kcal = dessert_all[i][dessert]
        drink_kcal = drink_all[i][drink]
        total_consumed += entree_kcal + dessert_kcal + drink_kcal
        print("| " + f"{count}".ljust(9) + "| " + entree.ljust(19) + "| " + dessert.ljust(19) + "| " + drink.ljust(15) + "|")
        count += 1

    print(li_mid)
    print("| " + "Exercises Logged".ljust(67) + " |")

    total_burned = 0
    count = 1
    for i in exercise_day:
        key = list(i.keys())[0]
        value = i[key]
        total_burned += value
        print("|  " + f"{count}. {key}".ljust(47) + f"({value} kcal burned)".ljust(19) + " |")
        count += 1

    print(li_mid)
    print("|" + "Totals".center(69) + "|")
    print(li_mid)
    print("| " + "Consumed:".ljust(16) + f"{total_consumed}".ljust(47) + "kcal |")
    print("| " + "Burned:".ljust(16) + f"{total_burned}".ljust(47) + "kcal |")
    print("| " + "TDEE Goal:".ljust(16) + f"{tdee}".ljust(47) + "kcal |")
    net_balance = total_consumed - total_burned - tdee - 1
    print("| " + "Net Balance:".ljust(16) + f"{round(net_balance)}".ljust(47) + "kcal |")
    print(li_down)
    print()


def show_full_history(db, tdee):
    """
    Display a summary of all logged meals and exercises.

    Args:
        db (dict): The database containing meals and exercises
        tdee (float): User's TDEE value
    """
    line = "─" * 45
    li_up = f"┌{line}┐"
    li_mid = f"├{line}┤"
    li_down = f"└{line}┘"

    days_logged = sorted(set(list(db["meals"].keys()) + list(db["exercises"].keys())))

    total_consumed = 0
    total_burned = 0

    print("\n--- Full History Summary ---\n")
    print("--- Daily Breakdown ---\n")

    for day in days_logged:
        meals = db["meals"].get(day, [])
        exercises = db["exercises"].get(day, [])

        daily_consumed = 0
        daily_burned = 0

        entree_all = meals[0:-1:3]
        dessert_all = meals[1:-1:3]
        drink_all = meals[2::3]

        for i in range(len(entree_all)):
            entree_kcal = list(entree_all[i].values())[0]
            dessert_kcal = list(dessert_all[i].values())[0]
            drink_kcal = list(drink_all[i].values())[0]
            daily_consumed += entree_kcal + dessert_kcal + drink_kcal

        for i in exercises:
            kcal = list(i.values())[0]
            daily_burned += kcal

        total_consumed += daily_consumed
        total_burned += daily_burned

        print(f"Date: {day}")
        print(f"  - Consumed: {daily_consumed} kcal | Burned: {daily_burned} kcal\n")

    days_count = len(days_logged)
    avg_consumed = round(total_consumed / days_count) if days_count else 0
    avg_burned = round(total_burned / days_count) if days_count else 0
    total_tdee = tdee * days_count
    overall_net = total_consumed - total_burned - total_tdee

    print(li_up)
    print("│" + "Overall Summary".center(45) + "│")
    print(li_mid)
    print("│ Days Logged:".ljust(30) + f"{days_count}".ljust(14) + "  │")
    print("│ Avg Daily Consumption:".ljust(30) + f"{round(avg_consumed):.0f}".ljust(9) + "  kcal │")
    print("│ Avg Daily Burn:".ljust(30) + f"{round(avg_burned):.0f}".ljust(9) + "  kcal │")
    print(li_mid)
    print("│ Total Consumed:".ljust(30) + f"{round(total_consumed)}".ljust(9) + "  kcal │")
    print("│ Total Burned:".ljust(30) + f"{round(total_burned)}".ljust(9) + "  kcal │")
    print("│ Total TDEE Goal:".ljust(30) + f"{total_tdee}".ljust(9) + "  kcal │")
    print("│ Overall Net Balance:".ljust(30) + f"{round(overall_net)}".ljust(9) + "  kcal │")
    print(li_down)
    print()


# Main part
import datetime

if __name__ == "__main__":
    db = {
        "meals": {},
        "exercises": {}
    }

    dash_long = "─" * 119  # 119
    line_long_up = f"┌{dash_long}┐"
    line_long_down = f"└{dash_long}┘"

    entree_keys = list(FOOD_DATA['entrees'].keys())
    dessert_keys = list(FOOD_DATA['desserts'].keys())
    drink_keys = list(FOOD_DATA['drinks'].keys())

    exercise_keys = list(EXERCISE_DATA.keys())

    invalid = "Invalid input."

    usr_name, usr_gender, usr_age, usr_weight, usr_height = ask_usr()
    usr_activity_level, usr_tdee = ask_activity_level(usr_name, usr_gender, usr_weight, usr_height, usr_age)
    usr_tdee = round(usr_tdee)
    while True:
        usr_choice = main_page()
        if usr_choice == 6:
            print(f"Goodbye, {usr_name}!")
            break

        elif usr_choice == 5:
            show_full_history(db, usr_tdee)

        elif usr_choice == 4:
            show_day_summary(db, usr_tdee)

        elif usr_choice == 3:
            remove_entry(db)

        elif usr_choice == 2:
            year, month, day, exercise_name, kcal_burn_per_hour, kcal_burned, dict_data = add_exercise()
            if f"{year}-{month}-{day}" not in list(db["exercises"].keys()):
                db["exercises"][f"{year}-{month}-{day}"] = dict_data
            else:
                for i in dict_data:
                    db["exercises"][f"{year}-{month}-{day}"].append(i)

        elif usr_choice == 1:
            year, month, day, meal_data = add_meal()
            if f"{year}-{month}-{day}" not in list(db["meals"].keys()):
                db["meals"][f"{year}-{month}-{day}"] = meal_data
            else:
                for i in meal_data:
                    db["meals"][f"{year}-{month}-{day}"].append(i)