name = "Abdul Rehman"
print(name.upper())   #dont change original String but return copy 
print(name)           #here again it will print original string
print(name.lower())  #same

print(name.find('l'))
print(name.find("Rehman"))  #substring

print(name.replace("Rehman","Rahim")) #dont change original String but return copy 

print("R" in name)  #Return True if R exist in name