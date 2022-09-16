#tuples basic
ordered=("Mangoes","Apples","oranges")
print(type(ordered))

#tuples modification
x=list(ordered)
print(type(x))
x.insert(1,"cliffe")
print(x)
ordered=tuple(x)
print(ordered)
print(type(ordered))

#tuples append also same
#tuples remove """"  """"
#we can append the tuples by using the above method

unordered=("matcher","puff")
ordered=ordered+unordered
print(ordered)
print(type(ordered))

#delete the tuple
del (unordered)
print(ordered)

#looping 
for w in ordered:
    print(w)

#unpacking tuples
(one,two,*three)=ordered
print(one)
print(type(one))
print(two)
print(type(two))
print(three)
#type conversion from list to tuple
print(type(three))
x=tuple(three)
print(type(x))


#looping in range and length
for x in range(len(ordered)):
    print(ordered[x])
i=0
while i<len(ordered):
    print(ordered[i])
    i=i+1


#condition checking
if "Mangoes" in ordered:
    print("yes it is present")

#methods for tuples are 1.count
x=(2,4,3,5,9,7,5,6)
print(x.count(5))
print(type(x))
#2.index (identifier)
x=(4,5,3,4,5,6,3,4,5)
print(x.index(5))








































    
