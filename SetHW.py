
gl1 = {"milk", "bread", "eggs", "apples"}
gl2 = {"bread", "eggs", "cheese", "bananas"}
gl3 = {"milk", "eggs", "bananas", "oranges"}

print("Grocery List 1:", gl1)
print("Grocery List 2:", gl2)
print("Grocery List 3:", gl3)

print("\nUnion:")
print(gl1 | gl2 | gl3)

print("\nIntersection:")
print(gl1 & gl2 & gl3)

print("\nDifference (List 1 - List 2):")
print(gl1 - gl2)
