import re

txt=str(input("Enter the text:"))
x=re.search("^The.*Matrid$",txt)
if x:
    print("X is verified")
else:
    print("X is not matching")
