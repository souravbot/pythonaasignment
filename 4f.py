# Q4 (f)
fruits = ["apple", "banana", "mango", "banana"]
x = input("Enter element to find: ")
if x in fruits:
    print("First occurrence of", x, "is at index", fruits.index(x))
else:
    print(x, "not found in list")
