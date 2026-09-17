#type conversion
x = 1
y = 2.4
c = "7" # isko int me convert karna hai to int(c) likhna padega float me convert karna hai to float(c) likhna padega type casting ka use karna padega
d = float("33")
z = x+y
print("value of z is:", z) #here float is superior value so int convert in float value
print(x+int(c))
print(type(int(c))) # type casting of string to int type casting possible only when string is number 
print(y+float(d)) # type casting of string to float
f = 3.14
f = str(f) # type casting of float to string explicit type casting of float to string
print(type(f)) 