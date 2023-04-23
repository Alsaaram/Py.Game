# Saram Nadeem Intro to Scripting

STARTING_POSITION = "Cave Start"

# Code below defines the rooms and which path each direction leads to when moving
rooms = {
    'Cave Start': {
        'South': 'Buried Temple',
        'North': 'Underground Forest',
        'East': 'Glowing Crystal Cavern',
        'West': 'Darth Mauls Room'
    },
    'Buried Temple': {
        'North': 'Cave Start',
        'East': 'Ritual Lair'
    },
    'Ritual Lair': {
        'West': 'Buried Temple'
    },
    'Glowing Crystal Cavern': {
        'North': 'Abandoned Mining Area',
        'West': 'Cave Start'
    },
    'Abandoned Mining Area': {
        'South': 'Glowing Crystal Cavern',
        'item': 'Keys'
    },
    'Underground Forest': {
        'South': 'Cave Start',
        'East': 'Buried Ship'
    },
    'Buried Ship': {
        'West': 'Underground Forest'
    },
    'Darth Mauls Room': {
        'East': 'Cave Start'
    }
}

# Creates and items and connects their locations to the places in the map
items = {
    'Buried Temple': 'Switch',
    'Ritual Lair': 'Bottom Hilt',
    'Glowing Crystal Cavern': 'Hilt Guard',
    'Abandoned Mining Area': 'Keys',
    'Underground Forest': 'Top Hilt',
    'Buried Ship': 'Kyber Crystal'
}

# Starting area
position = STARTING_POSITION


# For movement around the map
def get_new_position(new_position, direction):
    # What if the room or direction does not exist?

    # If you just return the existing position, how can the programme determine something went wrong?
    # The name of this function suggests a new state will be returned, which is misleading as it's not a guarantee.

    # Two approaches here:
    # 1. Before calling this function, validate that the position is and direction are valid inputs. If not, ask user
    #    for new ones. Or, use the validator inside this function.
    # 2. Validate inside this function and return a tuple. E.g. `return true, state`. Returning `true` will signal
    #    that it was valid request, and return the new state. Returning `false` will signal that it was invalid, and
    #    return the existing state. You will need to check for true and false after this is function is called. I don't
    #    know Python best practices, so not sure if this is a good approach or not. However, it is a common pattern
    #    in Go.

    # Personally, I would have a validator, which follows the Single Responsibility Principle.
    # See: https://en.wikipedia.org/wiki/Single-responsibility_principle

    # Below I've combined the two if statements with an `and` clause. Generally, nesting `if` statements is a code
    # smell, but it can't always be avoided. As a rule of thumb, aim for no nesting. Too many if statements is a sign of
    # too much being handled by a piece of code, and that functionality should be abstracted.

    # There was no need to loop over the rooms. It's not an array. It's a dictionary, which gives you instant lookups.
    # You just need the key to get the room and its directions. The key is being passed in to this function.
    # mind that it might not be valid.

    # You used `i` for looping. For arrays that is ok as it represents an index, but when looping over objects, you
    # should use `k` or `key`.

    room = rooms.get(new_position)
    if room and direction in room:
        return room[direction]
    
    raise ValueError("Invalid room or direction")


def get_items(state):
    return rooms[state]['items']


# Instructions for the text based game
def show_instructions():
    print('A Star Wars based Adventure Game!')
    print('Collect the six items and form a lightsaber to battle the evil Darth Maul!')
    print('To move, use the cardinal directions North, East, South, and West to travel around the map.')
    print('To pick up an item, type "Pick up part name".')


# Command to print the instructions as well as the inventory
show_instructions()
inventory = []

while 1:
    print('You are currently in the', position)  # Shows the current room
    print('Inventory', inventory)  # Shows the inventory
    item = get_items(position)
    print('Theres a part in the room, you found the', item)  # Identifies a part to the player
    if item == 'Darth Maul':
        print('Oh no! Darth Maul caught you! GAME OVER!!!')  # If room or part is Darth Maul, Player loses
        print('Play again to retry!')
        exit(0)
    direction = input('Which way do you want to go?')  # Direction options for users
    if direction == 'North' or direction == 'East' or direction == 'West' or direction == 'South':
        direction = direction[3:1]
        new_state = get_new_position(position, direction)
        if new_state == position:  # If the entered direction does not lead to an acceptable path
            print('You cant go that way, try another direction')
        else:
            position = new_state
    elif direction == str('Pick up' + item):  # Pick up the specified part in the room
        if item in inventory:
            print('You already have this item!')  # If the item is already held within the inventory
        else:
            inventory.append(item)  # Adds the item to the inventory
    else:
        print('You cant go that way!')
    if len(inventory) == 6:  # If all lightsaber parts are collected, leads to game end
        print('You collected all the parts required to build your lightsaber!')
        print('In an epic duel, you were able to escape the battle with Darth Maul and return to the Jedi Temple!')
        print("Thank you for playing!!!")
        exit(0)
