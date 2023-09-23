#accounts for if user does not put in correct int 



try: 
    number = int(input("Enter a number"))
    print(number)
    10/0
#be specif with except errors 
except ZeroDivisionError as err: 
    print(err)
except ValueError: 
    print("invalid input")