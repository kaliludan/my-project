import random

x = random.uniform(10, 20)

number = str(x + 0.5)
p = number.find(".")
change = number[0:p]

print x
print change