BURNED_CALORIES_PER_HOUR = {'aerobics': 600,
                            'badminton': 315,
                            'cycling': 560,
                            'housework': 215,
                            'running': 550,
                            'swimming': 420,
                            'walking': 230,
                            }
    
def compute_exercise_duration(_exercise, _excess_cal):

    full_minute = 60
    
    if _exercise in BURNED_CALORIES_PER_HOUR:
        for i in BURNED_CALORIES_PER_HOUR:
            if i == _exercise:
                kcal = BURNED_CALORIES_PER_HOUR[i]
                result = (_excess_cal * full_minute) / kcal
    
    return math.ceil(result)
    pass
         
import math   
print(compute_exercise_duration('cycling', 250))