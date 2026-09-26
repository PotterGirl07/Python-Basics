# variable can store a singular value 
# if you want to store multiple names, use LIST

names = ["Aashra","Brianna","Valeria","Ava","Maria"]
print(names)
#access an item from the list
print(names[0])
print(names[2])

#lists are mutable(changeable)
#lists have CRUD operation
#C-create, R-Read, U-Update, D-delete a list

#append- add an item to the end
names.append("Eva")
print(names)

#insert- at a specific index value
names.insert(3,"Nora")
print(names)

#read the list
for name in names:
    print(name)

#update the list
names[0] = "Aashra Dhakal"
print(names)

#delete (remove will take out item)
names.remove("Nora")
print(names)


#pop - can remove item with index value
name.pop(5)
print(names)