#moving items from one list to another

#start with users that need to be verified
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'cadance']
confirmed_users = []

#verify each users until there are no more unconfirmed users
#Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying User: {current_user.title()}")
    confirmed_users.append(current_user)

#display all confirmed users
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#HOW TO REMOVE ALL INSTANCES OF A VALUE FROM A LIST USING WHILE LOOP
pets = ['dog', 'cat', 'penguin', 'fish', 'cat', 'rabbit', 'cat', 'dog']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)


#POLLING PROGRAM TO GET INFO FOR DICTIONARY USING INPUT
responses = {}
#set a flag to indicate that polling is active
polling_active = True
while polling_active:
    #prompt for person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #store response in dictionary.
    responses[name] = response
    #find out is anyone else is going to take the poll.
    repeat = input("Whould you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
#polling is complete. show results
print("\n ---Polling Results!---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
