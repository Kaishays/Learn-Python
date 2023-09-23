#relative or absoulute path to file 
#"r" - read 
#"w" -write 
#"a" -append (add info to end)
#"r+" -read and write
#use open command
employee_file = open("employees.txt", "r")
#remeber to .close your file  
#check if file is .readable 

#.readline reads independent line 
#.readlines puts all lines on a list (can use array [1] for specic line)
print(employee_file.readable)
employee_file.close()