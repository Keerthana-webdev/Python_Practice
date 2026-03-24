#Create a new file "practice.txt" using python.Add the following data in it:
with open("practice.txt" , "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java")

#WAF that replace all occurrences of "java" with "python" in above file.
with open("practice.txt" , "r") as f:
    data = f.read()

new_data = data.replace("Java" , "Python")
print(new_data)

with open("practice.txt" , "w") as f:
    f.write(new_data)

#Search if the word "learning" exists in the file or not.
word= "learning"
with open("practice.txt" , "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found")

#OR 
def check_for_word():
    word= "learning"
with open("practice.txt" , "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found")

check_for_word()

#WAF to find in which line of the file does the word "learning" occur first.Print -1 if word not found.
def check_for_line():
    word= "like"
    data= True
    line_no=1
    with open("practice.txt" , "r") as f:
        while data:
            data= f.readline()
            if(word in data):
               print(line_no)
               return
            line_no += 1

    return -1

print(check_for_line())

#from a file containing numbers separated by comma, print the count of even numbers.
count =0
with open("practice1.txt" , "r") as f:
    data = f.read()

    nums=data.split(",")
    for val in nums:
        if(int(val) % 2==0):
            count +=1
    print(count)

