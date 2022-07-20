#Without Argument and without return value
"""
def user():
    print("hello world")
    print("\nnice to meet you")
user()
"""
#Without Argument and with return value
"""
a=10
b=10
def user():
    if a==b:
        return True
    else:
        return False
print(user())
"""
#With Argument and without return value
"""
def user(name,gender):
    if gender=="m":
        print("hello mr",name)
    else:
        print("hello mrs",name)
name=input("enter name here: ")
gender=input("enter gender here (m/f): ")
user(name,gender)
"""
#With Argument and with return value
"""
def user(a,b):
    if a==b:
        return "correct statement"
    else:
        return "inncorect statement"
print(user(a=input("enter a value here: "),b=input("enter b value here: ")))
"""