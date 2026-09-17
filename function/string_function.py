str = "hi I m Kasif Like python programming"
print(str.endswith("ing"))# here we check the string ends with "ing" or not
print(str.startswith("Hi"))# here we check the string starts with "Hi" or not
print(str.capitalize())# here we capitalize the first letter of the string but no change in the original string
str = str.capitalize() # so here we capitalize the first letter of the string and assign it to the original string
print(str) 
print(str.replace("o","a"))# here we replace the "o" with "a" but no change in the original string
print(str.replace("python","javascript"))
print(str.find("o"))# here we find the index of the first occurrence of "o" in the string
print(str.find("javascript"))# Agar koi string nhi hai usse find kro to - 1 aayega
print(str.find("python"))# agr pure word ko find kre to yaha uska starting index aayega
print(str.count("a"))# here we count the number of occurrences of "a" in the string
print(str.count("i"))