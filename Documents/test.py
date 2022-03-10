#String processing with different methods


string1 = "I am very happy"
string2 = "BABY"
string3 = "everyone wants to take their place"
string4 = " I'm a bip good ponighp"
string5 = " hello "
string6 = "1,2,3,4,5,6"
string7 = "toto est un totoo"

#Method of capitalizing a string of characters

string1 = string1.upper()
print(string1)

# Put in lower case

String2 = string2.lower()
print(string2)

  #  Capitalise the first character of the 
  #  beginning of a string. Be careful if the string 
  #  has several words, only the first character of the first word will change. 
  
string3 = string3.capitalize()
print(string3)

#To make the previous case effective on each word, use the following method. 
string3 = "everyone wants to take their place"
string3 = string3.title()
print(string3)


#replace with another character string, a word or a letter of another character string

string4 = string4.replace("p", "t")
print(string4) 

#delete a character with the .strip() method.
#Note that by default, this method removes the beginning and end spaces. 

#the first example is the removal of spaces
string5 = string5.strip()
print(string5)

#The second example shows how to specify the character to be removed. 
string5 = "ggxjhello "
string5 = string5.strip('gxjx')
print(string5) 


#recover a string to make a list

string6 = string6.split()
print(string6)




