weight = 87
height = 1.78

bmi = weight/ height**2

print(f'BMI: {bmi}')

# BMI	Category
# <= 18.5	Underweight
# 18.5 - 24.9	Normal
# 25 - 29.9	Overweight
# >= 30	Obesity

if bmi <= 18.5:
    print('You are Underweight')
elif 18.5<bmi<=24.9:
    print('You are Normal')
elif 25<bmi<=29.9:
    print('You are Overweight')
elif bmi>=30:
    print('You are Obesity')
else:
    print('Strange case')