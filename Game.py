# From the Unit and Item tabs you'll want to import the "Unit" and "Item".
# Doing so defines both the Player AND the Potion "inits" within the game.

from subprocess import call
import os
def  clear():
    call('clear' if os.name =='posix' else 'cls')
clear() 
    
from Unit import Unit, Player
from Item import Item, Potion

#name = input("What do you want the player to be named?\n")
name = "Waldo"
player = Player(name, [5,5])


# Here you'll be giving not only names for the enemies, but you'll also be setting the positions (coordinates) of enemies.
# This is called "looping through a nested list"
enemies = [
    Unit("Carmen Sandiego", [4,4], 10, 2),
    Unit("Inspector Gadget", [6,6], 6, 3)
]

items = [
    Item("Mike", [2,3]),
    Potion("Health Potion", [3,3])
]
# For this menu you'll be making a list that gives the directions in which they can move.
menu = ["Move up", "Move Down", "Move Left", "Move Right"]

def show_menu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    i += 2
    for item in player.inventory:
        print(f"{i}. Use {item.name}")
        i += 1


    
playing = True

while playing:
    print(player)
    show_menu()
    try:
        action = int(input("Choose your destiny!!\n"))
    except ValueError:
        print("You must enter a valid entry.")
        action = None

# These are actions defined by player/user movements. Set these sctions with "if", "elif", "else".

    if action:
        if action == 1:
            player.move("up")
        elif action == 2:
            player.move("down")
        elif action == 3:
            player.move("left")
        elif action == 4:
            player.move("right")
        else:
            if action-4 <= len(player.inventory):
                player.inventory[action-5].use()

# This shows that you've set the player/enemy positions (coordinates).
# The choice gives the player the option to either fight or run away if you land on the same spot as the enemy.

    for enemy in enemies:
        if enemy.position == player.position:
            choice = int(input('enter 1 to fight, 2 to run away \n'))
            if choice == 1:
                print(f"You ran into {enemy.name}:")
                print("You attack Shredder!")
                player.attack(enemy)
                print("Foot Clan attacks!")
                enemy.attack(player)
            else:
                print(f"You ran away from {enemy.name}:")

    for item in items:
        if item.position == player.position:
            if item.name == "Mike":
                playing = False
                print("You found Mike. You won the game.")
            else:
                print(f"You have come across {item.name}")
                player.pickup_item(item)

