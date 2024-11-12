#Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("Enter the num 1"))
num2 = int(input("Enter the num 2"))

Q = num1//num2
R = num1%num2

print("Quotient is : ", Q)
print("Remainder is : ", R)
