#Store following word meanings in a python dictionary:
# table: "a piece of furniture" , "list of facts & figures"
# cat: "a small animal"
dict={
   "cat": "a small animal" ,
   "table": ["a piece of furniture" , "list of facts & figures"]
}
print(dict)

#You are given a lsit of subjects for students. Assume one classroom is required for 1 subject.How many classrooms are noted by all students.
# "python", "java" , "c++" , "python" , "js" , "java" , "python" , "java" , "c++" , "c"
sub={
    "python", "java" , "c++" , "python" , "js" , "java" , "python" , "java" , "c++" , "c"
}
print(len(sub))

#Write a program to enter mars of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add 1 by 1.Use subject name as key & marks as value.
marks={}

x= int(input("Enter phy: "))
marks.update({"phy": x})

x= int(input("Enter math: "))
marks.update({"math": x})

x= int(input("Enter bio: "))
marks.update({"bio": x})

print(marks)

#Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in datatypes)
9 == 9.0 #True
k ={9 , 9.0}
print(k)
