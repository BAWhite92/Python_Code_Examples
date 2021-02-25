
bikes = ['trek', 'cannondale', 'carera', 'saxon']
print(bikes)

print (bikes[0])
print(bikes[2].title()) #is neater formatting, adds capitalisation

#using index of -1, python always returns last item in list
#can use -2, -3 etc to work backwards through list

print(bikes[-1].title())

#f strings formata nd create messages from variables
message = f"My bike is a {bikes[1].title()}."
print(message)

#to change element in list just provide new item you want it to have
bikes[2] = 'yamaha'
print(bikes)

bikes.append('carera')
print(bikes)

#can append items to an empty list which is intiialised with []

#can delete items with del
del bikes[0]
print(bikes)

#pop() removes the last item from a list but allows you to still work with that time, good for moving users from active to inactive lists etc works like stack! POP OFF TOP
print("break break")
popped_bikes = bikes.pop()
print(bikes)
print(popped_bikes)

#can pop any position using index
motorbikes = ["Yamaha", "Ducatti", "fast", "slow", "suzuki"]
first_bike = motorbikes.pop(2)
print(motorbikes)
print(f"My first bike was {first_bike}.")

#if you do not know position of an item you want to delete you can use remove() if you know value. 
print("remove method inc")
print(motorbikes)

motorbikes.remove('Ducatti')
print(motorbikes)

motorbikes.append('Ducatti')
print(motorbikes)
print('\nNow to give a reason for deletion of Ducatti')

too_expensive = 'Ducatti'
motorbikes.remove(too_expensive)
print(motorbikes)
print(f"\nA {too_expensive.title()} is too expensive for me")

#remove() only does 1st instance of value, use loops to remove more of the same value.


print("\n \n New area, organising a list")

#sort() permanently organises into alphabetcial

cars = ['bmw', 'audi', 'mclaren', 'ferrari', 'saab', 'alfa', 'landrover']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

#using reverse=True sorts in descending order instead.

#using sorted() temporarily sorts a list, will maintain original order of listy but present it in sorted format
print("\n \n")
cars = ['bmw', 'audi', 'mclaren', 'ferrari', 'saab', 'alfa', 'landrover']
print("Here is the original list: ")
print(cars)

print("\n Here is the sorted list which is temporary: ")
print(sorted(cars))

#can reverse the current order of the list by using reverse()
print("\n this is a reverse of the original list not in alpha order: ")
print(cars)
cars.reverse()
print(cars)

length = len(cars)
print(length)
