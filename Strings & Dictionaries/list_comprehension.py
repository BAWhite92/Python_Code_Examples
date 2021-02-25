#list comprehension, makes getting a list of value, key pairs in size order easy and in 1 line.
c = {"a":10, "b":1, "c":22}

print( sorted( [ (v,k) for k,v in c.items() ] ) )
#[] creates a list of value keys that appear in c as key:items pairs.
#as the (v,k) is expressed as a tuple that is how they are saved, MUST be tuple to do this.

#this gives a list in low toh igh order based in value amounts. due to sorted()
#can still use reverse = True

print( sorted( [ (v,k) for k,v in c.items() ], reverse = True) )


days= ( "Mond", "Tues", "Wed", "thur")
print(days[2])