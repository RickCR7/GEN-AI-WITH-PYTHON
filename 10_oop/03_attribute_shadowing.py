class Chai:
    temparature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temparature)

cutting.temparature = "mild"
cutting.cup = "small"
print(cutting.temparature)

del cutting.temparature
del cutting.cup
print(cutting.temparature) # falls back to class
print(cutting.cup) # gives error