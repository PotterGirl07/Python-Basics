#Dictionary is a data structure that stores key-value pairs together

stuRepCard={
    "Aashra":100,
    "Lucas":99,
    "Brianna":92,
    "Valeria":96,
    "Lochlann": 87,
}

# print(stuRepCard)

print(stuRepCard["Aashra"])
print(stuRepCard["Lucas"])

#update a key's value
stuRepCard["Brianna"]=97
print(stuRepCard["Brianna"])

print(stuRepCard.keys())
print(stuRepCard.values())

#pop/remove item
stuRepCard.pop("Lochlann")
#add new item
stuRepCard["Liam"]=98
print(stuRepCard)

#1) Merge 2 lists
#make lists
l1=["Math","ELA", "Science","History"]
l2=[100, 98, 96, 95]
#merge/join
result=dict(zip(l1,l2))
print(result)
#clear dictionary
result.clear()
print(result)


