#password strength checker
password = input("enter password: ")
#simple if else stmt
if len(password) < 8:
    print("password isnt lengthy enough")
else:
    print("password is strong")    