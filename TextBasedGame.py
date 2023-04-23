# Saram Nadeem Intro to Scripting

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
state = 'Cave Start'


# For movement around the map
def get_new_state(state, direction):
    new_state = state
    for i in rooms:
        if i == state:
            if direction in rooms[i]:
                new_state = rooms[i][direction]
    return new_state


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
    print('You are currently in the', state)  # Shows the current room
    print('Inventory', inventory)  # Shows the inventory
    item = get_items(state)
    print('Theres a part in the room, you found the', item)  # Identifies a part to the player
    if item == 'Darth Maul':
        print('Oh no! Darth Maul caught you! GAME OVER!!!')  # If room or part is Darth Maul, Player loses
        print('Play again to retry!')
        exit(0)
    direction = input('Which way do you want to go?')  # Direction options for users
    if direction == 'North' or direction == 'East' or direction == 'West' or direction == 'South':
        direction = direction[3:1]
        new_state = get_new_state(state, direction)
        if new_state == state:  # If the entered direction does not lead to an acceptable path
            print('You cant go that way, try another direction')
        else:
            state = new_state
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
