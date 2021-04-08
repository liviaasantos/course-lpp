print("This program calculates your body mass index.")

weight = float(input("Type your weight in Kg: "))
height = float(input("Type your height in m: "))

BMI = weight / ( height ** 2 )

print("Your BMI is: ", round(BMI,2))

if (BMI<=18.5):
    print("Underweight")
elif (BMI>18.5 and BMI<=24.9):
    print("Normal weight")
elif (BMI>24.9 and BMI<=29.9):
    print("Overweight")
else:
    print("Obesity")
