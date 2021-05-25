
pounds = float(input("Enter weight in pounds : "))
feet = float(input("Enter feet : "))
inches = float(input("Enter inches : "))
kilograms = pounds * 0.45359237
meters = inches * 0.0254 + feet * 0.3048
BMI = kilograms / (meters * meters)
print("BMI is ", BMI)
if BMI < 18.5:
    print("You are Underweight")
elif BMI < 24.9:
    print("You are Normal")
elif BMI < 29.9:
    print("You are Overweight")
elif BMI > 30.0:
    print("You are Obese")
else:
    print("Bilinmeyen hata")
