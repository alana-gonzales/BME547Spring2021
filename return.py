def my_function(x):
    a = x + 5
    if x < 0:
        answer = "Negative number"
    else:
        answer = "Positive number"
    return a, answer

y = my_function(-20)
print(y[0])
print(y[1])

# OR
# y, z = my_function(-20)
# print(y)
# print(z)

# 'return' ends the program as soon as it hits a return statement
