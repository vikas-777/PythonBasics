# Amstrong number
num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
