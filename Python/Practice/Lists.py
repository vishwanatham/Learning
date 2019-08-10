fruits = ["Banana", "Apple", "Custard Apple"]

print("length of the list is " + str(len(fruits)))

fruits.append("Mango")

print("After appending a new fruit")

print(fruits)

fruits.insert(0, "Guava")

print("After inserting "+fruits[0] + "fruit at " + str(fruits.index("Guava")) + " position")

print(fruits)
