gl1 = {"milk", "bread", "eggs", "apples"}
gl2 = {"bread", "eggs", "cheese", "bananas"}
gl3 = {"milk", "eggs", "bananas", "oranges"}

print("Grocery List 1:", gl1)
print("Grocery List 2:", gl2)
print("Grocery List 3:", gl3)

print(" ")

print("Union:")
print(gl1 | gl2 | gl3)

print(" ")

print("Intersection:")
print(gl1 & gl2 & gl3)

print(" ")

print("Difference (List 1 - List 2):")
print(gl1 - gl2)
