# Q4 (b)
fruits = ["apple","banana","orange"]
pos = int(input("Enter position (0 to {}): ".format(len(fruits))))
if 0 <= pos <= len(fruits):
    element = input("Enter element to insert: ")
    fruits.insert(pos, element)
print("After insert:", fruits)
