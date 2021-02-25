favorite_languages = {
    'jen' : 'python',
    'ben' : 'python',
    'sarah' : 'c',
    'jogn' : 'ruby',
}

print("The following languages are mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    #stops any repeats of languages by using set

print("\nThe people who participated are:")
for people in sorted(favorite_languages):
    print(f"\t{people.title()}")
    #using f allows formatting of the people and \t tabs the line in for neatness!
    #for a dictionary iterating over the keys is the standard behavour.

fave_languages = {
    'jen' : ['python', 'c'],
    'ben' : ['python'],
    'sarah' : ['c', 'ruby'],
    'jogn' : ['ruby', 'python'],
}

for name, languages in fave_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")