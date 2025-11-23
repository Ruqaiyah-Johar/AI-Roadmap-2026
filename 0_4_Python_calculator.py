# Python calculator

operator = input("enter an operator(+ - * /): ")
number1 = float(input("enter your 1st number: "))
number2 = float(input("enter your 2nd number: "))
if operator == "+":
    result = number1 + number2
    print(round(result, 3))
elif operator == "-":
    result = number1 - number2
    print(round(result, 3))
elif operator == "*":
    result = number1 * number2
    print(round(result, 3))
elif operator == "/":
    result = number1 / number2
    print(round(result, 3))
else:
    print(f"{operator} isnt a valid operator")

# Python BMI calculator

age = int(input("age in years : "))
gender = input("gender Male/ Female (M/F): ")
gender = gender.upper()

weight = float(input("enter your weight: "))
unit = input("please specify, Kilograms or Pounds (K/ P): ")
unit = unit.upper()  # normalize input

if unit == "P":
    weight = weight / 2.205
    unit = "Kgs"
elif unit == "K":
    unit = "Kgs"
else:
    print(f"{unit} was not valid")
    exit()

height = float(input("enter your height: "))
measurement = input(
    "please specify the unit, meters or cm of feet or inches(m/cm/f/in): ")
measurement = measurement.lower()

if measurement == "cm":
    height = height / 100
    measurement = "m"
elif measurement == "f":
    height = round(height * 0.3048, 3)
    measurement = "m"
elif measurement == "in":
    height = round(height * 0.0254, 3)
    measurement = "m"
elif measurement == "m":
    height = height * 1
    measurement = "m"
else:
    print(f"{measurement} is not a valid measurement")
    exit()
print(
    f"you are {age}/{gender}, weighing {weight}{unit} with a height of {height}{measurement}.")
querry = input("is that correct? yes/no : ")
querry = querry.lower()
if querry == "yes":
    new_height = height * height
    BMI = round(weight / new_height, 2)
else:
    print("sorry, the data you entered is wrong :( )")
    exit()
print(f"your BMI is {BMI}")
if BMI <= 18.5:
    print("your BMI category is underweigh. ")
elif 18.5 <= BMI <= 24.9:
    print("your BMI category is normal weight")
elif 25.0 <= BMI <= 29.9:
    print("your BMI category is over weight")
elif 30.0 <= BMI <= 34.9:
    print("your BMI category is Obesity Class I")
elif 35.0 <= BMI < 39.9:
    print("your BMI category is Obesity Class II")
elif BMI >= 40.0:
    print("your BMI category is Obesity Class III")
else:
    print("try again")
