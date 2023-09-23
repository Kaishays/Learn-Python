#define a class and inheriant its traits into a new class
class Chef:
    def make_chicken(self): 
        print("The chef makes a chicken")
    
    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a special dish")

from Chef import Chef

