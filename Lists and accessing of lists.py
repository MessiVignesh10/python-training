ordered=["Banana","Egg rice",65,"Veg noodles"]
print(ordered)
print(ordered[2:5])
print(ordered[1])
print(ordered[2])
print(type(ordered))
if 65 in ordered:
    print("yes it is in the ordered")
# To change the contents in the list
# use the index values

ordered[1]="Chicken rice"
print(ordered)
print(type(ordered[2]))

# inserting the list items
ordered.insert(1,"watermelon")
print(ordered)

#append the list items
ordered.append("Chocolate")
print(ordered)

#extend the list
unordered=("egg noodles","Chappathi")
ordered.extend(unordered)
print(ordered)

#remove the list item
ordered.remove(65)
print(ordered)

#remove the specific item in the list using the pop option
ordered.pop(1)
print(ordered)

#normally no specify value in the pop means it pops out the last value in the list
ordered.pop()
print(ordered)

#clear is used to clear the entire list

#ordered.clear()
#print(ordered)


#del is used to delete the value in the list
print(ordered)
del ordered[1]
print(ordered)

#-------------------------------------------------------------------------------------------------------
#looping through lists
for x in ordered:
    print(x)
    

#lopping by the range and length of the list
for x in range(len(ordered)):
    print(ordered[x])

#looping in while loop
i=0
while i<len(ordered):
    print(ordered[i])
    i=i+1
#--------------------------------------------------------------------------------------------------------
# sorting of lists

print(ordered)
ordered.sort()
print(ordered)
ordered.sort(reverse=True)
print(ordered)
ordered.sort(key = str.lower)
print(ordered)
ordered.sort(key = str.upper)
print(ordered)

#--------------------------------------------------------------------------------------------------------
#copying the entire list
delivery=ordered.copy()
delivery.append("Success")
print(delivery)

#--------------------------------------------------------------------------------------------------------
#joining the lists
unavailable=[23,4,5,6,43]
notdelivered=ordered+unavailable
print(notdelivered)

#another method
for x in ordered:
    unavailable.append(x)
    print(unavailable)
#last method
ordered.extend(unavailable)
print(ordered)































































