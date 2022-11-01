
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))



BMI = round(weight / (height**2))
if BMI <= 18:
    print(f"your BMI is {BMI}, You are underweight." )
elif BMI >18 and  BMI < 25:
    print(f"your BMI is {BMI}, You have a normal weight." )

elif BMI >= 25 and BMI < 30:
    print(f"your BMI is {BMI}, You are slightly overweight." )

elif BMI >= 30 and BMI < 35:
    print(f"your BMI is {BMI}, You are obese." )

elif BMI >= 35:
    print(f"your BMI is {BMI}, You are clinically obese." )