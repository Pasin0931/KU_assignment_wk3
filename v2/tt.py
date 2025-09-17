def ask_usr():
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

    print(f"Profile created for {username}. Your TDEE is {tdee} kcal.\n")
    return activity_level


def main_page():
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
                print("Please enter a number between 1-6.")
        except ValueError:
            print()
            print(invalid)


invalid = "Invalid input."

usr_name, usr_gender, usr_age, usr_weight, usr_height = ask_usr()
usr_activity_level = ask_activity_level(usr_name, 100)
main_page()