import random
import art
import Char_Stats
import Events
import Inventory
import time
from replit import clear

#todo 0 define variables for char stats, monster stats and treasure location
char_HP = Char_Stats.current_HP
char_attack = Char_Stats.attack
char_def = Char_Stats.armor
enemy_name = ""
enemy_HP = 0
enemy_attack = 0
enemy_def = 0
char_defending = False
enemy_defending = False
treasure_location = random.choice(Events.events)
treasure_found = False
decision = ""
location = ""
#todo 1 define character stats and allow for changes in the stats in a function
def Pick_enemy():
  '''Uses global variable manipulation to select what the enemy will be and update the stats accordingly'''
  enemy = random.choice(Events.monsters)
  global enemy_name 
  enemy_name =  enemy["Name"]
  global enemy_HP 
  enemy_HP =  enemy["HP"]
  global enemy_attack 
  enemy_attack =  enemy["Attack"]
  global enemy_def
  enemy_def =  enemy["Armor"]
  # print(enemy_name)
  # print(enemy_HP)
  # print(enemy_attack)
  # print(enemy_def)
  
def Dmg_roll(enemy_atk, char_armor, defend):
  '''calculates the damage done to your target when you attack and return the amount of damage done'''
  if defend == True:
    dmg = round(enemy_atk * (10/(10 + (char_armor*2))))
    return dmg
  else:
    dmg = round(enemy_atk * (10/(10 + char_armor)))
    return dmg
   
def Update_hp(current,dmg):
  '''update the hp of the character and return the hp after the round'''
  current -= dmg
  return current

Pick_enemy() #pick first random enemy
def Battle():
  turn_order = 1
  option = ""
  global char_attack
  global char_HP
  global char_def
  global char_defending
  global enemy_HP
  global enemy_attack
  global enemy_def
  global enemy_defending
  global enemy_name
  dmg = 0
  battle_rages = True
  while battle_rages:
    clear()
    print(f"Player: {char_HP}HP -- {enemy_name}: {enemy_HP}HP")
    if turn_order % 2 != 0 and enemy_HP > 0:
      option = input("Would you like to (A)ttack or (D)efend?: ").lower()
      if option == "d":
        char_defending = True
        print("You brace yourself.")
        time.sleep(2)
        turn_order += 1
      elif option == "a":
        if char_defending:
          char_defending = False
        dmg = Dmg_roll(char_attack, enemy_def, enemy_defending)
        enemy_HP = Update_hp(enemy_HP, dmg)
        if enemy_HP > 0:
          print(f"You swing wildly at the {enemy_name} and land a blow dealing {dmg} to the {enemy_name}\nThe {enemy_name} has {enemy_HP}HP remaining")
          turn_order += 1
          time.sleep(2)
        elif enemy_HP <= 0:
          battle_rages = False
          print(f"You swing wildly at the {enemy_name} and land a blow dealing {dmg} to the {enemy_name}\nThe {enemy_name} has been slain!")
      else:
        print("I didn't understand your command, try again.")
        time.sleep(3)
    elif turn_order % 2 == 0 and char_HP > 0:
      dmg = Dmg_roll(enemy_attack, char_def, char_defending)
      char_HP = Update_hp(char_HP,dmg)
      if char_HP > 0:
        print(f"The {enemy_name} attacks you and lands a hit!\nIt deals {dmg} to you.\nYou have {char_HP}HP left.")
        time.sleep(3)
        turn_order += 1
      elif char_HP <= 0:
        battle_rages = False
        print(f"The {enemy_name} deals a deadly blow.\nThe world grows dark and you feel the last ounce of your strength leave you.\nOh dear you are dead.......")
    else:
      time.sleep(2)
  


location = random.choice(Events.events)
print("Welcome to treasure hunter!\nYour goal is to seek the treasure of the king.\nGood luck and may the fates be on your side!")
time.sleep(5)
while not treasure_found:
  location = random.choice(Events.events)
  clear()
  print(f"Player: {char_HP}HP\nYou come upon {location}")
  time.sleep(2)
  if location == treasure_location:
    treasure_found = True
    print("Congratulations you have found the treasure!!")
  else:
    Pick_enemy()
    print(f"A {enemy_name} attacks you!")
    time.sleep(3)
    Battle()