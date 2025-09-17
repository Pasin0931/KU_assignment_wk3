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
    
    print(f"│{15 * " "}│{15 * " "}|")
    print(line_long_down)


def format_entree_data(data):
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
    line_1 = data[0:-1:5]
    line_2 = data[1:-1:5]
    line_2.append(data[-1])
    
    
    count = 1
    for i in range(0, len(line_1)):
        line_1[i] = f"{count}. {line_1[i]}"
        count += 5
        
    count = 2
    for i in range(0, len(line_2)):
        line_2[i] = f"{count}. {line_2[i]}"
        count += 5
    
    print(line_long_up)
    
    for i in line_1:
        print(f"|  {i:<21}", end="")
    print("|")
    
    for i in line_2:
        print(f"|  {i:<21}", end="")
    print("|")
    
    print(line_long_down)
    

dash_long = "─" * 100 #119
line_long_up = f"┌{dash_long}┐"
line_long_down = f"└{dash_long}┘"

entree_keys = list(FOOD_DATA['entrees'].keys())
dessert_keys = list(FOOD_DATA['desserts'].keys())
drink_keys = list(FOOD_DATA['drinks'].keys())

format_entree_data(entree_keys)
format_dessert_drink_data(dessert_keys)
format_dessert_drink_data(drink_keys)
    

# def ask_usr():
#     print("--- Setting up your profile ---")

#     while True:
#         name = input("Enter your name: ")
#         if name == "":
#             print(invalid)
#         else:
#             break

#     while True:
#         gender = input("Enter your gender (M/F): ").upper()
#         if gender == "M" or gender == "F":
#             break
#         else:
#             print(invalid)

#     while True:
#         try:
#             age = int(input("Enter your age: "))
#             if age > 0:
#                 break
#             else:
#                 print(invalid)
#         except ValueError:
#             print(invalid)

#     while True:
#         try:
#             weight = float(input("Enter your weight (kg): "))
#             if weight > 0:
#                 break
#             else:
#                 print("Weight must be positive.")
#         except ValueError:
#             print(invalid)

#     while True:
#         try:
#             height = float(input("Enter your height (cm): "))
#             if height > 0:
#                 print()
#                 break
#             else:
#                 print("Height must be positive.")
#         except ValueError:
#             print(invalid)

#     return name, gender, age, weight, height


# def ask_activity_level(username, tdee):
#     while True:
#         print("--- Activity Level ---")
#         print("1. Sedentary (little or no exercise)\n" \
#             "2. Lightly active (1-3 workouts/week)\n" \
#             "3. Moderately active (4-5 workouts/week)\n" \
#             "4. Very active (6-7 workouts/week)\n" \
#             "5. Extremely active (physical job or training)")
        
#         try:
#             activity_level = int(input("Choose your activity level (1-5): "))
#             if activity_level > 0 and activity_level < 6:
#                 print()
#                 break
#             else:
#                 print()
#                 print("Please enter a number between 1-5.")
#         except ValueError:
#             print()
#             print(invalid)

#     print(f"Profile created for {username}. Your TDEE is {tdee} kcal.\n")
#     return activity_level


# def main_page():
#     while True:
#         print("--- Main Menu ---")
#         print("1. Add Meals\n"
#               "2. Add Exercise\n"
#               "3. Remove an Entry\n"
#               "4. Show Summary for a Day\n"
#               "5. Show Full History\n"
#               "6. Exit")
#         try:
#             choice = int(input("Enter your choice: "))
#             if choice > 0 and choice < 7:
#                 break
#             else:
#                 print("Please enter a number between 1-6.")
#         except ValueError:
#             print()
#             print(invalid)
            
#     return choice


# def add_meal(player):
#     print("--- Adding Your Meals ---")
#     while True:
#         try:
#             ymd = input("Enter the date (YYYY-MM-DD): ").split("-")
#             if type(int(ymd[0])) == int and type(int(ymd[1])) == int and type(int(ymd[2])) == int:
#                 break
#             else:
#                 print("Please enter proper date.")
#         except ValueError:
#             print(invalid)


# if __name__ == "__main__":
#     invalid = "Invalid input."

#     usr_name, usr_gender, usr_age, usr_weight, usr_height = ask_usr()
#     usr_activity_level = ask_activity_level(usr_name, 100)
#     while True:
#         usr_choice = main_page()
#         if usr_choice == 6:
#             print(f"Goodbye, {usr_name}!")
#             break
#         if usr_choice == 5:
#             print("Nigger\n")
#         if usr_choice == 4:
#             print("Nigger\n")
#         if usr_choice == 3:
#             print("Nigger\n")
#         if usr_choice == 2:
#             print("Nigger\n")
#         if usr_choice == 1:
#             add_meal(usr_name)
#             print("Nigger\n")