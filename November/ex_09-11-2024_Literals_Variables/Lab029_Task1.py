# Task for the Today
# Take a 3 input from the user
# perform the sub, sub, mul and div

num1 = float(input("Enter the num 1"))
num2 = float(input("Enter the num 2"))
num3 = float(input("Enter the num 3"))

int()

sum = num1 + num2 + num3
sub = num1 - num2 - num3
mul = num1 * num2 * num3
if num2 != 0 and num3 != 0:
    div = num1 / num2 / num3
else:
    div = "Undefined (division by zero)"

print("Sum is : ", sum)
print("Sub is : ", sub)
print("Mul is : ", mul)
print("Div is : ", div)
