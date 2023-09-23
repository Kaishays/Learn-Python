#makes code more organized and powerful 
#can make your own data type

#what all the objects are 
#object represents an acutal object, student in this example 
#object - Instance within the class 
from student import student

student1 = student("Jim", "Business", 3.1, False)
student2 = student("Pam", "Art", 2.5, True)

print(student1.major)
print(student2.is_on_probation)