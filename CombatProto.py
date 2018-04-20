import random
import time
import os

#functions that will be commonly used
def roll():
    dice = random.randint(1,20)
    return dice
def enemyRoll():
    turn1 = random.randint(1,20)
    return turn1
def pause():
    programPause = input('Press Enter to continue...')

#hp values are set here    
monster_hp = 500
player_hp = 100

while monster_hp > 0 and player_hp > 0:
    print ('Your turn. Deus Vult!')
    print('You damaged the enemy for ' + str(roll()))
    monster_hp = monster_hp - roll()
    print("Enemy's remaining HP: " + str(monster_hp))
    time.sleep(1) #pauses the game for a second then proceeds
    print("\n")
    if monster_hp > 0:
        print("Enemy's turn.")
        print('Enemy damaged you for ' + str(enemyRoll()))
        player_hp = player_hp - enemyRoll()
        print('Remaining HP: ' + str(player_hp))
        print("\n")
    pause()#references fuction made earlier

    if monster_hp <= 0:
        print ("You have slain the monster. +2 exp")
        break
    if player_hp <= 0:
        print("you have died. git gud.")
        break

      
