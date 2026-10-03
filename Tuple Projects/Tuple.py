# tuples are a collection of items
# they cannot be changed
# therefore called inmuteable
# they are ordered, means all items have indexes
# these items can be of diverse data types 
# called Heterogeneous


subs=("English", "Math", "History", "Science")
print(subs)
print(subs[0])
print(subs[-2])

print(" "*3)

#packing a tuple
address=(123, "Made Up Street", "Skibidi Town", "Baddie City", "Gross State", "Rizzler Country", "152152")
print(address)

#unpacking a tuple
hno, street, town, city, state, country, postalcode = address
print(town)

print (" " *3)

s1 = ("Lucas", 13, "Columbus", "Spanish")
s2 = ("Aashra", 12, "Gahanna", "Spanish")

name, age, city, language = s1
print(name)
print(f"- {age}")
print(f"- {city}")
print(f"- Learning {language}")

name, age, city, language = s2
print(name)
print(f"- {age}")
print(f"- {city}")
print(f"- {language}")