#list give name, use sq brackets for list 
#   can use bulions or num in list
friends = ["Kevin", "Karen", "Jim", "Kai", "Tate","Ty"]

#use bracksts after varible for index 
#can use -1 for jim 
print(friends[0])
#use colon for all values after num including num 
print(friends[1:])
#use num colon num to give a range no including last num
print(friends[1:3])
#can change list values by 
friends[1] = "Kai"


#Functions in lists 

 
lucky = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Kai", "Tate","Ty"]

#extend concatinate two lists
friends.extend(lucky)
print(friends)
#append add indipendent name to list 
friends.append("Creed")
print(friends)
#insert individual at certain index 
friends.insert(1, "Kelly")
#remove individual from list
friends.remove("Jim")
#remove all
#friends.clear
print(friends)
#pop item off end of list 
friends.pop
#index certain value in list 
print(friends.index("Kevin"))
#count number of individuals on list 
print(friends.count("jim"))
#sort list
#friends.sort()
#print(friends)
#reverse a list 
lucky.reverse()
print(lucky)
#copy a list 
lucky2 = lucky.copy()
print(lucky2)