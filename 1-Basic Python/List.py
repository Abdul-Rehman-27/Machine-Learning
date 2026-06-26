marks = [90,70]
print(marks)
print(marks[0])
print(marks[-1]) # Reverse or from back side 
print(marks[0:2])    # 2 not included

marks.append(99)    #Add at the end
print(marks)

marks.insert(2,85)    #Add where u want
print(marks)

print(85 in marks)

print(len(marks))

marks.clear()   # Remove all element
print(marks)