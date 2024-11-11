name = "This is a testing commit"
print(type(name))
name = name + str(10)  # can only concatenate str (not "int") to str
print(name)

first_name = "Sachin"
last_name = "Kothari"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))