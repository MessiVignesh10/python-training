ordered={"1":"Mangoes","2":"Oranges","3":"Apples","4":"Tomatoes"}
print(type(ordered))
print(ordered["1"])
ordered ["5"]="Bananas"
print(ordered)
print(ordered["5"])

# keys sends the list of keys
print(ordered.keys())

#value command displays all the values
print(ordered.values())

#item commands displays  key:value pairs
print(ordered.items())

#check if key exists and we are not able to check the values
if "2" in ordered:
    print("Yes it is present in the dictionary")
else:
    print("no it is not present in the dictionary")


ordered["5"]="Maroon"
print(ordered)

ordered.update({"3":"Glitch"})
print(ordered)

#remove the dictionary items
print(ordered.pop("2"))

#del dictionary
del ordered["3"]
print(ordered)

#clear command empties the dictionary
#ordered.clear()
#print(ordered)

#dictionary looping
for x in ordered:
    print(ordered[x])
for x,y in ordered.items():
    print(x,y)
for x in ordered.values():
    print(x)
for x in ordered.keys():
    print(x)

# copy of Dictionaries
mydict=ordered.copy()
print(mydict)

#another way of copying
mydic=dict(ordered)
print(mydic)

#nested dictionaries
my_family={
    "Child 1":{
        "name":"Vignesh",
        "age":"22"
        },
    "Child":{
        "name":"Walter",
        "age":"20"
        }
       }
print(my_family)
print(type(my_family))
print(my_family["Child 1"])






















