#for loop can iterate over all items in a list.

magicians = ["bob", "bill", "houdini", "dave"]
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!\n")
    #although you can use any name best to use meaningful name.
print("That's the end of the show!\n")

#range makes it easy to generate a series of numbers
for value in range(1, 7):
    print(value)
print("this is using range! Notice it is off by one, it stops at 7 so only counts/prints to 6!\n")
#passing range through with no start number will cause it to start at 0

numbers = list(range(1, 6))
print(numbers)
print("this is a list created from using range\n")

#can give range steps such as finding even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print("by adding in steps to the range function it can be used to find even numbers\n")

#to find first 10 square numbers ** is exponent
squares = []
for value in range(1, 11):
    #square = value ** 2 (is longer version)
    squares.append(value ** 2)
print(squares)
print("created using for and range to find first 10 square numbers \n")


#list comprehension lets you condense the 3 or so lines shown above into 1 line of code
squares_comp = [value**2 for value in range(1, 11)]
print(squares_comp)
print("this is a comprehensively created version of previous code\n")

#can slice lists to work with only a part of the list!
players = ["ben", "scott", "charles", "martin", "chow", "brendan"]
print(players[0:3])
print("this is a slice of a longer list of players\n")



print(players[1:4])
print("another slice of the players\n")
#if no index is offered for start slice will auto start at 0

#can still loop through slices as well
print ("first 3 players are")
for player in players[:3]:
    print(player.title())
print("These guys are the best\n")

#can use slice to create a copy of a list by omitting first and second index, using = will point your variables to the same list!
print("I can copy my list \n")
players_new = players[:]
print("original")
print(players)
print("\n new list of players")
print(players_new)
print("\n both are the same!\n")
