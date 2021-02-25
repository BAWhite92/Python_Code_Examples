def greet_user(username):
        """Display a simple greeting."""
        print(f"Hello, {username.title()}!")

greet_user('ben')

#positional arguments
def describe_pet(pet_name, animal_type = 'dog'):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('Roger', 'cat')
describe_pet('barry')

#KEYWORD ARGUMENTS
describe_pet(animal_type = 'Rhino', pet_name = 'horn')
describe_pet(pet_name = 'josh', animal_type = 'cat')
#explicitly set the argument parameters, order does not matter
describe_pet(pet_name = 'raffe')
#defaut values can be set for parameters as seen for animal_type and for
# "barry" as seen above also, the default is supplied by the function for barry
