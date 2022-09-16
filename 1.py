x="Vignesh"
txt="My name is {}"
y=x.encode(encoding="ascii", errors="ignore")
print(txt.format(x))
print(y)
