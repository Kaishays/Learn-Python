#dictionaries - store values in key value pairs

#use json object 
#must use unique keys in dict
monthconversions = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    }
print(monthconversions["Apr"])
#.get - prints non if non or can print string 
print(monthconversions.get("Luv", "Not a valid Key"))
