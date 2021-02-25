def greet_users(names):
    """Print a simple greeting to each user in a list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ben', 'ty']
greet_users(usernames)



#modify a list in a function
#Start with some designs that need to be printed
def print_models(unprinted_designs, completed_models):
    """simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """display all completed"""
    print(f"\nThe following models have been completed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
#using [:] send a copy of a list to the function so that the original list
#is not altered in any way during execution. ONLY USE IF THERE IS A REASON TO
