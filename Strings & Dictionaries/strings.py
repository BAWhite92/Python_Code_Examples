name = "ADA LOVELACE"
print(name.title())

#title makes 1st letter uppercase and all other letters lowercase

print(name.upper())
print(name.lower())

first_name = "ben"
last_name = "white"
full_name = f"{first_name} {last_name}"
print(full_name)

#using f inserts variable's value into the string full_name can do a lot with f which stands for format

print(f"Hello, {full_name.title()}!")

print("ben \n is \n \t slowly \n \t \t moving \n out??")

#whitespace can affect string sbut rstrip() removes it from right side! *CLICK on results to see removal*

language = 'python  '
print(language)

language = language.rstrip()
print(language)
#lstrip() and strip() also used for left and all whitespace respectively

