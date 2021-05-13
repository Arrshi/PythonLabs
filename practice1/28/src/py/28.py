from sympy.ntheory import factorint


list = factorint(int(input()))
str = str(list)
str = str.replace(": 1", "", len(list))
str = str.replace(": ", "^", len(list))
str = str.replace(", ", " * ", len(list))
str = str.replace("{", "")
str = str.replace("}", "")
print(str)