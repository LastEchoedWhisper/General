import random


def diceRoll():
    dice = random.randint(1,20)
    print (dice)
    if dice < 10:
        print ("Unlucky, you take damage equal to the amount of your roll.")
    elif dice == 10:
        print ("You succesfully parried and took no damage.")
    elif dice > 10:
        print ("You damage enemy for the amount of your roll.")
    elif dice == 20:
        print ("You landed a critical hit! Multiply damage from roll by 1.5")

print (diceRoll())
        
