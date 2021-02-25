#a tuple is a list that is immutable, cannot be changed

#just use () instead of []
dimensions =  (200, 50)
print(dimensions[0])
print(dimensions[1])
print("\n")

#tuples are actually defined through use of commas, if only one element is in a tuple use comma after (trailing)

my_t = (3,)
print(my_t)
print("This tuple was created by using 3, as the comma created the tuple, brackets justmake it readable")
print(my_t[0])
print("\n")

for dimension in dimensions:
    print(dimension)
print("you can loop through tuples as well!\n")

#if you want to write over a tuple you can create a new tuple and assign it to the original tuple's variable

