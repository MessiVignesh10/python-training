try:
    print(X)
except NameError:
    print("Hii from NameError")
except:
    print("Hii from Others")
# the finally statement prints what default value is present in the final
finally:
    print("The try except block is finished")
#Raise Exception
x=3
if x>1:
    raise Exception("Sorry no numbers is below zero")
