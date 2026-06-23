word = {
      '1' : 'ONE' ,
      '2' : 'TWO' ,
      '3' : 'THREE' ,
      '4' : 'FOUR' ,
      '5' : 'FIVE' ,
      '6' : 'SIX' ,
      '7' : 'SEVEN' ,
      '8' : 'EIGHT' ,
      '9' : 'NINE' ,
      '0' : 'ZERO' ,
      }
num = input("Phone:   ")
output = ""
for x in num:
      output += word.get(x) + "  "

print(output)      
print(num)

print("Thank you for using Keerthana Softwares")      
      
           