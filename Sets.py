#define the set using the curly braces
ordered={"mangoes","Apple","oranges","papaya"}
print(type(ordered))
unordered=set(("cliifs","cradles"))
print(type(unordered))

#to add the list
unordered.add("lessi")
print(unordered)

#to update the list
ordered.update(unordered)
print(ordered)

#to  remove set items
ordered.remove("lessi")
print(ordered)

#to pop out
x=ordered.pop()
print(x)

#no usage here only for checking remberence
x=["vikki","vjkrish",63]
print(isinstance(x,str))
x=x.pop(1)
print(x)
print(isinstance(x,str))

#update sets
x={'a','b','c',34,"rty"}
y={"String","Character","integer"}
x.update(y)
print(x)

#update method 2 using Union
x={'a','b','c',34,"rty"}
y={"String","Character","integer"}
x=x.union(y)
print(x)


# just for remeberance
x=('a','b','c',34,"rty")
y=("String","Character","integer")
z=list(x)
w=list(y)
w.extend(z)
print(w)
w=tuple()
print(type(w))

#The intersection_update() method will keep only the items that are present in both sets.

x={'a','b','c',34,"rty"}
y={"String","Character","integer",34}

x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.

x={'a','b','c',34,"rty"}
y={"String","Character","integer",34}

z=x.intersection(y)
print(z)
print(x)
print(y)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x={'a','b','c',34,"rty"}
y={"String","Character","integer",34}

x.symmetric_difference_update(y)
print(x)

m=x.symmetric_difference(y)
print(m)










































