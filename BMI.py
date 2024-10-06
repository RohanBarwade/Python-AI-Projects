#BMI calculator
import matplotlib.pyplot as plt

print("welcome to rohan's BMI Calculator")

height=float(input("enter your height in metres: \n"))
weight=int(input("enter your weight in kg: \n"))

BMI=weight/(height*height)

if BMI < 18.5:
        Status= "Underweight"
elif 18.5 <= BMI < 24.9:
        Status= "Normal"
elif 25 <= BMI < 29.9:
        Status= "Overweighted"
else:
        Status= "Obese"


x_axis = ("Your BMI", "Normal BMI")
y_axis= [BMI,21.0]


plt.bar(x_axis, y_axis)


plt.xlabel(Status)
plt.ylabel('BMI')
plt.title("WELCOME TO ROHAN'S BMI CALCULATOR")

plt.show()