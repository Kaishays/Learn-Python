#Boolean variable 
def Boolean():
    is_male = True 
    is_tall = True 
#or
    if is_male or is_tall: 
        print("You are a male or tall or both")
    else: 
        print("You are not a male or tall")
#and 
    if is_male and is_tall: 
        print("You are male and tall")
        #else 
    else: 
        print("efhakl")

#Elif - use for multiple if satements in same function 
def Elif():
    is_female = True 
    is_tall = True
    if is_female: 
        print("you are female")
        
    elif is_female and not(is_tall):
        print("you are female and not tall")

#compare if statements 
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3: 
        return num2
    else: 
        return num3 

print(max_num(3, 40, 5))