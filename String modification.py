x="Vignesh"
txt="My name is {name} and age is {age}".format(name="Vignesh",age=22)
y=x.encode(encoding="ascii", errors="ignore")
print(txt.format(x))
print(y)
print(y.center(20))
print(txt.center(40))
