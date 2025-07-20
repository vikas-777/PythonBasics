num1 = int(input("Enter the number1..."))
num2 = int(input("Enter the number2..."))
operator = input("Choose operator (+,-,*,/,%)\t")
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif operator == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Choose the correct operator")
