#"Tuple Out" Dice Game
import random
# Ask player to roll the dice
print("Roll the dice")

# Roll the dice
roll = random.choices([1,2,3,4,5,6], k=3)
print(roll)

# Set the points variable
points = 0

# Set the answer variable to run the first time
answer = "Yes"

# For each turn:
# ask the person if they want to re-roll third die
# if player answers yes, re-roll third die
# when third die is re-rolled, replace the original value with the new value of third die
# since the player answered yes, they go through the loop again
# if 2 dice are the same, give player option to re-roll third dice
# if all dice are different, give player option to re-roll all of them at once (easier)
# if the player answers yes, it goes through the loop again <-- store "yes" into a variable and 
# use the variable in a while loop
# if the player answers no, it breaks out of the loop and prints out the results
while answer == "Yes":
    if roll[0] == roll[1] == roll[2]:
        print("Tuple Out! You receive zero points. Your turn is over.")
        break
    if roll[0] == roll[1] or roll[0] == roll[2] or roll[1] == roll[2]:
        if roll [0] == roll[1]:
            points = roll[0] + roll[1] + roll[2]
            index = 2
        if roll[0] == roll[2]:
            points = roll[0] + roll[1] + roll[2] 
            index = 1
        if roll[1] == roll[2]:
            points = roll[0] + roll[1] + roll[2]
            index = 0
        print(f"Two of the dice are fixed and cannot be rerolled. Your current dice score is: {roll} and your point value is: {points}")
        answer = input("Would you like to re-roll one of the die?")
        if answer == "Yes":
            new_value = random.sample([1,2,3,4,5,6], k=1)
            roll[index] = new_value[0]
        if answer == "No":
            print(f"Game over. Your total dice score is: {roll} and your point value is: {points}")
            break
    if roll[0] != roll[1] != roll[2]:
        points = roll[0] + roll[1] + roll[2]
        print(f"All numbers of the dice are different. Your current dice score is: {roll} and your point value is: {points}")
        answer = input("Would you like to re-roll all of the dice?")
        if answer == "Yes":
            roll = random.choices([1,2,3,4,5,6], k=3)
        if answer == "No":
            print(f"Game over. Your total dice score is: {roll} and your point value is: {points}")
            break