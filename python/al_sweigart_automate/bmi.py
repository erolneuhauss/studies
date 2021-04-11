#!/usr/bin/env python
# BMI = (weight in kg / height in meters squared)
# Imperial version: BMI * 703
def gather_info():
    """
    Gather height, weight und used measurement system
    """
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are your measurements in metric or imperial units? " +
                   "Type eigher 'm' for metric or 'i' for imperial units. ")\
                            .lower().strip()
    return (height, weight, system)

def calculate_bmi(height, weight, system='m'):
    """
    Return the Body Mass Index (BMI) for the
    given weight, height, and measurement system.
    """
    if system == 'm':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system == 'i':
        bmi = str(calculate_bmi(height=height, weight=weight, system=system))
        print(f"Your BMI is {bmi}")
        break
    elif system == 'm':
        bmi = calculate_bmi(height, weight)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error. Unknown measurement system. " +
              "Please use imperial or metric")
