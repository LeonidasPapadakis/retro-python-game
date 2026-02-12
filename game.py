#!/usr/bin/python3

from map import floors
from player import *
from items import *
from gameparser import *
from npcs import *
import random
import time
import threading
import sys
 

#prints a clear message to the player between two lines
def print_lines():
    #global variable for message to be displayed
    global message

    #clear the screen
    print("\n"*40)
    print("""
/(,-.   )\.---.   )\  )\   )\.---.     /`-.   .-,.-.,-.      .'(       .-,.-.,-.      .'(   )\.---.          /(,-.     .-./(   )\  )\   )\.---.    )\.--.  
 ,' _   ) (   ,-._( (  \, /  (   ,-._(  ,' _  \  ) ,, ,. (  ,') \  )      ) ,, ,. (  ,') \  ) (   ,-._(       ,' _   )  ,'     ) (  \, /  (   ,-._(  (   ._.' 
(  '-' (   \  '-,    ) \ (    \  '-,   (  '-' (  \( |(  )/ (  '-' (       \( |(  )/ (  '-' (   \  '-,        (  '-' (  (  .-, (   ) \ (    \  '-,     `-.`.   
 )  _   )   ) ,-`   ( ( \ \    ) ,-`    )   _  )    ) \     ) .-.  )         ) \     ) .-.  )   ) ,-`         )  _   )  ) '._\ ) ( ( \ \    ) ,-`    ,_ (  \  
(  '-' /   (  ``-.   `.)/  )  (  ``-.  (  ,' ) \    \ (    (  ,  ) \         \ (    (  ,  ) \  (  ``-.       (  '-' /  (  ,   (   `.)/  )  (  ``-.  (  '.)  ) 
 )/._.'     )..-.(      '.(    )..-.(   )/    )/     )/     )/    )/          )/     )/    )/   )..-.(        )/._.'    )/ ._.'      '.(    )..-.(   '._,_.'  
                                                                                                                                                              """)
    #print the message in a box
    if len(message) > 0:
        print("-"*140)
        for line in message:
            print(line)
        print("-"*140)

        #reset the message
        message = []

#takes a list of items and a list of keys to display, and prints a string displaying the items and their stats if they if exist, returns weight of all items
def item_stats(items, keys):

    #weight counter
    weight = 0
    
    #loop through items
    for item in items:
        print("-"+item["name"].upper()+"-")

        #start a line of text in which the stats will be displayed
        line =""

        #loop through keys
        for key in keys:

            #if the key exists, add to the line
            if key in item.keys():
                line = line + key.upper() +": "+str(item[key])+" / "
    
        print(line)
        print(item["description"]+"\n")

        #Add item's weight to total
        weight = weight + item["weight"]
    return weight
    


#takes a list of stats and a list of their titles, and prints them in a nice box like this:
# = = = = = = = = = = = = = = = = =
# = Your Health = Enemy's Health  =
# =     100     =       20        =
# = = = = = = = = = = = = = = = = =
def print_box(stats, titles):

    #start each line
    title_line = "= "
    stat_line = "= "
    
    #loop through the lists
    index = 0
    while index < len(titles):

        #add the length of either the title or stat (whichever is bigger) to the count and modify each line
        if len(titles[index]) >= len(str(stats[index])):
            title_line = title_line + titles[index] + " = "

            spaces = len(titles[index]) - len(str(stats[index]))
            stat_line = stat_line + " "*(spaces // 2) + str(stats[index]) + " "*(spaces - (spaces // 2)) + " = "

        #in the case that the stat is longer than the title   
        else:
            stat_line = stat_line + str(stats[index]) + " = "

            spaces = len(str(stats[index])) - len(titles[index])
            title_line = title_line + " "*(spaces // 2) + titles[index] + " "*(spaces - (spaces // 2)) + " = "
            
        index = index + 1

    #if length is even, add an extra space to make sure the box matches up nicely
    if len(title_line) % 2 != 0:
        title_line = title_line[:len(title_line) -2] + " ="
        stat_line = stat_line[:len(stat_line) -2] + " ="

    #print the box
    if len(title_line) % 2 == 0:
        print("= "*(len(title_line)//2))
    else:
        print("= "*(len(title_line)//2 +1))
        
    print(title_line)
    print(stat_line)

    if len(title_line) % 2 == 0:
        print("= "*(len(title_line)//2))
    else:
        print("= "*(len(title_line)//2 +1))

#creates a 2d array for the map layout
def map_layout(room, xPos, yPos):

    #add current rooms name and exits to the map
    layout[xPos][yPos] = [room["name"], room["exits"]]
    #print(layout)

    #loop through current room exits
    for key in room["exits"].keys():

        #for each exit, calls function recursively
        if key == "north" and layout[xPos-1][yPos] == 0 and floors[room["exits"][key]]["Floor"] == room["Floor"]:
            map_layout( floors[room["exits"][key]], xPos-1, yPos)
            
        elif key == "east" and layout[xPos][yPos+1] == 0 and floors[room["exits"][key]]["Floor"] == room["Floor"]:
            map_layout( floors[room["exits"][key]], xPos, yPos+1)
            
        elif key == "south" and layout[xPos+1][yPos] == 0 and floors[room["exits"][key]]["Floor"] == room["Floor"]:
            map_layout( floors[room["exits"][key]], xPos+1, yPos)
            
        elif key == "west" and layout[xPos][yPos-1] == 0 and floors[room["exits"][key]]["Floor"] == room["Floor"]:
            map_layout( floors[room["exits"][key]], xPos, yPos-1)


#prints a nice map for the player like this:
#  ~~~~~~~~~~~~~~~~~~~~~~~~
# | ###########  ######### |
# | #         #  #       # |
# | # Entance  ==  Room2 # |
# | #         #  #       # |
# | #####  ####  ###  #### |
# |      ||         ||     |
# | #####  ####  ###  #### |
# | #         #  #       # |
# | #  Room3  #  # Room4 # |
# | #         #  #       # |
# | ###########  ######### |
#  ~~~~~~~~~~~~~~~~~~~~~~~~
def print_map():

    #create a global variable
    global layout, message

    print_lines()

    #set map dimensions here
    mapX = 4
    mapY = 4

    #new 2d array and call map layout function to add the maps layout
    layout = [[0 for x in range(mapX)] for y in range(mapY)]

    if current_room["Floor"] == 1:
        map_layout(floors["room1"], 0, 3)
    elif current_room["Floor"] == 2:
        map_layout(floors["room10"], 0, 2)
    elif current_room["Floor"] == 3:
        map_layout(floors["room18"], 0, 2)

    #create new list for lines
    lines = ["|" for y in range(len(layout)*6-1)]
    lines.append("")
    
    #loop through each y coordinate
    for y in range(0, mapY):

        #set a value to determine the lagrest set of characters
        largest = 0

        #loop through x coordinates to find largest character length
        for x in range(0, mapX):
            if layout[x][y] != 0:
                
                #if largest length so far, update largest
                if len(layout[x][y][0]) > largest:
                    largest = len(layout[x][y][0])

        #loop through x values
        for x in range(0, mapX):
            if layout[x][y] != 0:

                #add the name to the list with a corresponding amount
                #of spaces either end (sorry for the wierd maths)
                name = " "*( (largest - len(layout[x][y][0]) ) // 2 ) + layout[x][y][0] + " "*((largest - len(layout[x][y][0]) )- ( (largest - len(layout[x][y][0]) ) // 2 ))

                #if there is an exit to the north add a passage, if not add a wall
                if "north" in layout[x][y][1].keys():
                    lines[x*6] = lines[x*6] + " "+"#"*((largest+4)//2-1)+"  "+"#"*(largest+3-(largest+4)//2)+" "
                else:
                    lines[x*6] = lines[x*6] + " "+"#"*(largest+4)+" "

                #if there is an exit to the west add a passage, if not add a wall
                if "west" in layout[x][y][1].keys():
                    lines[x*6+1] = lines[x*6+1] + "-#"
                    lines[x*6+2] = lines[x*6+2] + "  "
                    lines[x*6+3] = lines[x*6+3] + "-#"
                else:
                    lines[x*6+1] = lines[x*6+1] + " #"
                    lines[x*6+2] = lines[x*6+2] + " #"
                    lines[x*6+3] = lines[x*6+3] + " #"

                
                lines[x*6+1] = lines[x*6+1] +" "*(largest+2)
                
                #add the name of the room
                if layout[x][y][0] == current_room["name"]:
                    lines[x*6+2] = lines[x*6+2] + ">"+name.upper()+"<"
                else:
                    lines[x*6+2] = lines[x*6+2] + " "+name+" "

                lines[x*6+3] = lines[x*6+3] + " "*(largest+2)

                #if there is an exit to the south add a passage, if not add a wall
                if "south" in layout[x][y][1].keys():
                    lines[x*6+4] = lines[x*6+4] + " "+"#"*((largest+4)//2-1)+"  "+"#"*(largest+3-(largest+4)//2)+" "
                    lines[x*6+5] = lines[x*6+5] + " "+" "*((largest+4)//2-2)+"|  |"+" "*(largest+2-(largest+4)//2)+" "
                else:
                    lines[x*6+4] = lines[x*6+4] + " "+"#"*(largest+4)+" "
                    lines[x*6+5] = lines[x*6+5] + " "*(largest+6)

                #if there is an exit to the east add a passage, if not add a wall
                if "east" in layout[x][y][1].keys():
                    lines[x*6+1] = lines[x*6+1] + "#-"
                    lines[x*6+2] = lines[x*6+2] + "  "
                    lines[x*6+3] = lines[x*6+3] + "#-"
                else:
                    lines[x*6+1] = lines[x*6+1] + "# "
                    lines[x*6+2] = lines[x*6+2] + "# "
                    lines[x*6+3] = lines[x*6+3] + "# "

            #if no room here
            else:
                lines[x*6] = lines[x*6] + " "*(largest+6)
                lines[x*6+1] = lines[x*6+1] + " "*(largest+6)
                lines[x*6+2] = lines[x*6+2] + " "*(largest+6)
                lines[x*6+3] = lines[x*6+3] + " "*(largest+6)
                lines[x*6+4] = lines[x*6+4] + " "*(largest+6)
                lines[x*6+5] = lines[x*6+5] + " "*(largest+6)

    #print a little compass
    print("")
    print(" "*(len(lines[0])//2)+          "N"      )
    print(" "*(len(lines[0])//2)+          "|"      )
    print(" "*(len(lines[0])//2-3)+     "W -+- E"   )
    print(" "*(len(lines[0])//2)+          "|"      )
    print(" "*(len(lines[0])//2)+          "S"      )

    #add a nice border
    for i in range(0, len(lines)-1):
                lines[i] = lines[i] + "|"
    lines[len(lines)-1] = " "+"~"*(len(lines[1])-2) +" "     
    print("\n "+"~"*(len(lines[1])-2) +" ")
    
    #print the map
    for line in lines:
        print(line)

    #Give options
    print("\nYou can:")
    
    # Iterate over available exits
    exits = current_room["exits"]
    lockedExits = []
    if "locked" in current_room.keys():
        lockedExits = current_room["locked"]
    for direction in exits:

        if direction not in lockedExits:
        # Print the exit name and where it leads to
            print_exit(direction, exit_leads_to(exits, direction))
        
    print("CLOSE to close your map.")
    print("What do you want to do?")

    #read and normalise player's input
    user_input = input("> ")
    user_input = normalise_input(user_input)

    #go commands
    if user_input[0] == "go":
        if len(user_input) > 1:
            execute_go(user_input[1])
        else:
            message.append("Go where?")

    #stops calling the print inventory function if the user types close
    elif user_input[0].lower()== "close":
        message.append("You close your map.")

    #re-opens inventory if nothing is selected
    else:
        message.append("This makes no sense.")
        print_map()


        
    
#saves the games state at a checkpoint
def set_checkpoint(): 
    global checkpoint
    checkpoint = {"inventory":inventory,
        "coins":coins,
        "weight_limit":weight_limit,
        "escape_chance":escape_chance,
        "health":health,
        "max_health":max_health,
        "damage":damage,
        "mana":mana,
        "current_room":current_room,
        "previous_room":previous_room,
        "floors":floors,
        "npcs":npcs}
                            
    

#this is called when the players health reaches 0
def death():
    
    while True:
        message.append("You are dead. Re-run game to play again.")
        print_lines()
        input()



def print_room_items(room):
    
    if len(room["items"]) > 0:
        print("Items in this location:\n")
        
        #loop through each item in the room and print out its details.
        for item in room["items"]:
            print("-"+item["name"].upper()+"-")
            line = ""
            if "damage" in item.keys():
                line = line + "Damage: "+str(item["damage"])+" / "
            line = line + "Value: "+str(item["value"])+" / Weight: "+str(item["weight"])
            print(line)
            print(item["description"]+"\n")

def combat(enemy):
    global health
    global mana
    global current_room, previous_room, damage, message
    global in_combat
    
    print("You are under attack by "+enemy.name+"!")
    print("You may not advance until the threat has been dealt with!\n")

    #display player's and enemy's health:
    print_box([health, enemy.health], ["Your Health", enemy.name+" Health"])
    
    #give player options
        
    print("\nYou can:")

#options for attacking the monster

    for item in inventory:
        if "damage" in item.keys():
            print("ATTACK "+item["id"].upper() + " to attack with your " + item["name"]+".")
    for item in inventory:
        if "effects" in item.keys():
            print("DRINK "+item['id'].upper()+" to drink a "+item["name"]+".")
    print("OPEN INV to take a look at your inventory")
    if enemy.name!="Hans":
        print("RUN to attempt an escape.")
   
    print("What do you want to do?")

    #read and normalise player's input
    user_input = input("> ")
    user_input = normalise_input(user_input)


    

    if len(user_input) != 0:
        if user_input[0] == "attack":
            if len(user_input) > 1:
                found = False

                #loop through each item in the players inventory
                for item in inventory:
                    if user_input[1] == item["id"] and "damage" in item.keys():
                        found = True

                       #subtract item damage from enemies health
                        hit_damage = int(item["damage"] * damage)
                        damage = 1.0

                        enemy.health = enemy.health - hit_damage
                        message.append("You attacked "+enemy.name+" with "+item["name"]
                                    +" and did "+str(hit_damage)+" damage!")

                        #if enemy was killed
                        if enemy.health<=0:


                            current_room["npcs"].remove(enemy)
                            
                            message.append(f"{enemy.name} has been defeated!")
                            
                            for item in enemy.items:
                                current_room["items"].append(item)
                                message.append(f"{enemy.name} has dropped {item['name']}")

                            #unlock exits if enemy has speech options
                            if enemy.speech != "":
                                if "exits" in enemy.speech.keys() and "locked" in current_room.keys():
                                    for locked_exit in enemy.speech["exits"]:
                                        if locked_exit in current_room["locked"]:
                                            current_room["locked"].remove(locked_exit)
                                            message.append("A passage to the "+locked_exit+" has been unlocked")
                            

                            #this resets the enemies health once killed , so when you encounter the enemy again their health wont be 0
                            for npc in npcs:
                                if npc==enemy.name:
                                    enemy_previous_health=(npcs[enemy.name][1]["health"])
                                    enemy.health=enemy_previous_health
                        else:
                            enemy_attack(enemy)

                        break
                        
                #if the user wants to attack a weapon that they do not have, print an error
                if found == False:
                    message.append("You cannot attack with '"+user_input[1]+"'.")
                    
            else:
                message.append("Attack with what?")

        #potion options
        elif user_input[0].lower() == "drink":

            #if potion selected
            if len(user_input) > 1:

                #loop through inventory
                found = False
                for item in inventory:

                    #if item is a potion and matches the potion selected
                    if "effects" in item.keys() and user_input[1] == item["id"]:
                        found = True

                        #loop through and apply each potion effect
                        for effect in item["effects"].keys():

                            #health effects
                            if effect == "health":

                                #if drinking would put player over maximum health
                                if health + item["effects"]["health"] > max_health:
                                    health = max_health
                                else:
                                    health = health + item["effects"]["health"]

                            #damage multiply effects
                            elif effect == "damage":
                                damage = damage * item["effects"]["damage"]

                        #remove from inventory and break
                        message.append("You drank a "+item["name"]+".")
                        inventory.remove(item)
                        break         
                        
                #if no matching potion found, print an error
                if found == False:
                    message.append("You cannot drink '"+user_input[1]+"'.")

            else:
                message.append("Drink what?")
            
        #command to open inventory
        elif user_input[0].lower() == "open":
            if len(user_input) > 1:
                if user_input[1] == "inv":
                    message.append("You open your inventory")
                    print_inventory_items(inventory)
                else:
                    message.append("You cannot open '"+user_input[1]+"'.")


        #if player chooses to escape, they have a chance to escape successfully,
        #or suffer an attack and remain in place
        elif user_input[0].lower() == "run":
            rand = random.randint(1,100)

            #if successful, update current room
            if rand <= escape_chance:
                message.append("You escaped "+enemy.name+" successfully.")
                temp = previous_room
                previous_room = current_room
                current_room = temp

            #if unsuccessful, trigger an enemy attack
            else:
                message.append("You tried to escape "+enemy.name+" but you were unsuccessful.")
                enemy_attack(enemy)
        else:
            message.append("This makes no sense.")

        
    
    
#this function is called when an enemy is attacking the player
def enemy_attack(enemy):
    global health, message

    #1 in 10 chance of 150% critical hit
    rand = random.randint(1, 10)
    if rand == 1:
        damage = int(enemy.damage * 1.5)
        message.append("Critical hit! "+enemy.name+" attacked you doing "+str(damage)
                    +" points of damage!")
    else:
        damage = enemy.damage
        message.append(enemy.name+" attacked you doing "+str(damage)
                    +" points of damage!")
        

    #subtract damage from player's health
    health = health - damage

#function for speaking to a neutral npc
def speak_enemy(enemy):
    global current_room

    #if npc has diologue options
    if enemy.speech != "":
        for line in enemy.speech["diologue"]:
            message.append(line)
            print_lines()
            input("> ")
        speech = ""
            
        #loop through enemys speech options
        for index in range(0, len(enemy.speech["questions"])-1, 2):

            question = enemy.speech["questions"][index]
            #PlayLongSound(enemy.SpeechSound[0])
            answer = enemy.speech["questions"][index+1]
            message.append(enemy.name+": '"+question+"'")

            print_lines()

            #if expected response is a string, ask for user input
            if type(answer) == str:
                print("You can type your response below:")
                user_input = input("> ")

                #we don't want to use the normalise input function as that could remove words important to answering a riddle
                user_input = remove_punct(user_input).lower()

                #if correct
                if user_input == answer:

                    #print pass diologue
                    message.append(enemy.name+": '"+enemy.speech["pass"]+"'")
                    #PlayLongSound(enemy.SpeechSound[1])
                    #unlock exits
                    for npc in current_room["npcs"]:
                        if npc.id == enemy.id:
                            npc.aggression = "passive"
                    if "exits" in enemy.speech.keys() and "locked" in current_room.keys():
                        for locked_exit in enemy.speech["exits"]:
                            if locked_exit in current_room["locked"]:
                                current_room["locked"].remove(locked_exit)
                                message.append("A passage to the "+locked_exit+" has been unlocked")
                            
                    return

                
        #if incorrect
        message.append(enemy.name+": '"+enemy.speech["attack"]+"'")
        for npc in current_room["npcs"]:
            if npc.id == enemy.id:
                npc.aggression = "aggressive"
        

#function for buying and selling at a merchant
def speak_merchant(player_items, merchant):
    global Played
    global coins

    message.append(merchant.name+" - 'This is what I have to offer.'")
    print_lines()

    if len(merchant.items) > 0 :

        #print merchant items 
        weight = item_stats(merchant.items, ["damage", "value", "weight"])


    else:
        print("\n"+merchant.name+" - 'Sorry, I have nothing in stock'\n")

    if len(player_items) > 0:
        
        #print the player's inventory:
        print("Your items:\n")
        weight = item_stats(player_items, ["damage", "value", "weight"])

        print("TOTAL CARRY WEIGHT: "+ str(weight) +"/"+str(weight_limit))

    else:
        print("Your inventory is empty")

    #print available coins
    print("COINS: "+str(coins)+"\n")



    #give options for player input
    merchantSpeech="You can"
    print("You can:")
    #options for buying items
    for item in merchant.items:
        print("BUY "+item["id"].upper() + " to buy " + item["name"]
              +" for " + str(item["value"]) + " coins.")
        
        merchantSpeech+=("BUY "+item["id"].upper() + " to buy " + item["name"]
              +" for " + str(item["value"]) + " coins.")

    #options for selling items
    for item in player_items:
        print("SELL "+item["id"].upper() + " to sell " + item["name"]
              +" for " + str(item["value"]) + " coins.")
        
        merchantSpeech+=("SELL "+item["id"].upper() + " to sell " + item["name"]
              +" for " + str(item["value"]) + " coins.")
        
    print("CLOSE to leave the merchant.")
    print("What do you want to do?")

    #read and normalise player's input
    user_input = input("> ")
    user_input = normalise_input(user_input)

    if len(user_input) != 0:

        #if the player wishes to buy something
        if user_input[0] == "buy":
            if len(user_input) > 1:
                found = False

                #loop through each item in the merchants inventory
                for item in merchant.items:
                    if user_input[1].lower() == item["id"].lower():
                        found = True

                        #if the item will fit in player's inventory
                        if item["weight"] + weight <= weight_limit:
                        
                            #if the player can afford the item
                            if coins >= item["value"]:

                                #add to player's inventory and remove from merchant's
                                inventory.append(item)
                                merchant.items.remove(item)
                                coins = coins - item["value"]
                                
                                message.append("You bought "+item["name"]+" for "
                                            +str(item["value"])+" coins")
                                speak_merchant(inventory, merchant)
                                
                            else:
                                message.append("You cannot afford this.")
                                speak_merchant(inventory, merchant)
                            
                            #break to avoid items being bought twice
                            break

                        else:
                            message.append("Item is too heavy. Drop or sell something from your inventory.")
                            speak_merchant(inventory, merchant)


                #if the user wants to buy an item that is not available, print an error
                if found == False:
                    message.append("You cannot buy '"+user_input[1]+"'.")
                    speak_merchant(inventory, merchant)
                    
            else:
                message.append("Buy what?")
                speak_merchant(inventory, merchant)


                        
            #if the user wants to buy an item that is not available, print an error
            if found == False:
                
                message.append("You cannot buy '"+user_input[1]+"'.")
                speak_merchant(inventory, merchant)


        #if the player wishes to sell something
        elif user_input[0] == "sell":

            if len(user_input) > 1:
                found = False

                #loop through each item in the players inventory
                for item in player_items:
                    if user_input[1] == item["id"]:
                        found = True

                        #remove from player's inventory and add to merchant's
                        merchant.items.append(item)
                        inventory.remove(item)
                        coins = coins + item["value"]

                        message.append("You sold "+item["name"]+" for "
                                    +str(item["value"])+" coins")
                        speak_merchant(inventory, merchant)

                        #break to avoid items being sold twice
                        break

                #if the user wants to sell an item that they do not have, print an error
                if found == False:
                    message.append("You cannot sell '"+user_input[1]+"'.")
                    speak_merchant(inventory, merchant)
                    
            else:
                message.append("Sell what?")
                speak_merchant(inventory, merchant)


        #stops calling the function if the user types close merchant
        elif user_input[0] == "close":
            message.append("You leave the merchant.")

                             
        #re-opens merchant if nothing is selected
        else:
            message.append("Sell what?")
            speak_merchant(inventory, merchant)
                            
    #re-opens merchant if nothing is selected
    else:
        message.append("This makes no sense.")
        speak_merchant(inventory, merchant)

      

#new function for printing the player's inventory
def print_inventory_items(items):
    global health, damage, message, inventory, current_room

    #display message
    print_lines()

    #Display health and coins
    print("\n")
    print_box([health, coins, damage], ["HEALTH", "COINS", "DAMAGE X"])

    #display inventory
    if len(inventory) > 0:
        print("\nYour inventory:\n")
    else:
        print("\nYour inventory is empty.") 
      
    weight = item_stats(items, ["damage", "value", "weight"])

    print("TOTAL CARRY WEIGHT: "+ str(weight) +"/"+str(weight_limit))

    #give options for player input
    print("\nYou can:")
    for item in inventory:
        print("DROP "+item["id"].upper() + " to drop your " + item["name"]+".")
    for item in inventory:
        if "effects" in item.keys():
            print("DRINK "+item['id'].upper()+" to drink a "+item["name"]+".")
    for item in inventory:
        if "contents" in item.keys():
            print("READ "+item['id'].upper()+" to read "+item["name"]+".")
    print("CLOSE to close your inventory.")
    print("What do you want to do?")

    #read and normalise player's input
    user_input = input("> ")
    user_input = normalise_input(user_input)

    if 0 == len(user_input):
        return

    #calls the drop function if the player chooses drop
    if user_input[0].lower() == "drop":
        if len(user_input) > 1:
            execute_drop(user_input[1])
            print_inventory_items(inventory)
        else:
            message.append("Drop what?")
            print_inventory_items(inventory)

    #read command
    elif user_input[0].lower() == "read":
        if len(user_input)> 1:
            found = False
            
            #loop through inventory
            for item in inventory:
                
                if user_input[1].lower() == item["id"] and "contents" in item.keys():

                    found = True
                    message.append(item["contents"])

                    #unlock exits
                    if "exits" in item.keys():
                        if current_room["name"] in item["exits"].keys():
                            locked_exit = item["exits"][current_room["name"]]
                            print(locked_exit)
                            current_room["locked"].remove(locked_exit)
                            item["exits"][current_room["name"]] = ""
                            message.append("A passage to the "+locked_exit+" has been unlocked.")

                    #break to stop on item
                    break
                
            if found == False:
                message.append("You cannot read '"+user_input[1]+".")
            print_inventory_items(inventory)
        else:
            message.append("Read what?")
            print_inventory_items(inventory)

            

    #stops calling the print inventory function if the user types close
    elif user_input[0].lower()== "close":
        message.append("You close your inventory.")

    #potion options
    elif user_input[0].lower() == "drink":

        #if potion selected
        if len(user_input) > 1:

            #loop through inventory
            found = False
            for item in inventory:

                #if item is a potion and matches the potion selected
                if "effects" in item.keys() and user_input[1] == item["id"]:
                    found = True

                    #loop through and apply each potion effect
                    for effect in item["effects"].keys():

                        #health effects
                        if effect == "health":

                            #if drinking would put player over maximum health
                            if health + item["effects"]["health"] > max_health:
                                health = max_health
                            else:
                                health = health + item["effects"]["health"]

                        #damage multiply effects
                        elif effect == "damage":
                            damage = damage * item["effects"]["damage"]

                    #remove from inventory and break
                    message.append("You drank a "+item["name"]+".")
                    inventory.remove(item)
                    break         
                    
            #if no matching potion found, print an error
            if found == False:
                message.append("You cannot drink '"+user_input[1]+"'.")
                
            print_inventory_items(inventory)
        
        else:
            message.append("Drink what?")
            print_inventory_items(inventory)
        
    #re-opens inventory if nothing is selected
    else:
        message.append("This makes no sense.")
        print_inventory_items(inventory)        


#function for printing npcs in a room
def print_npcs(room):
    if len(room["npcs"]) > 0:

        #variable to check if there are any aggressive anemies, if so the other npcs will not be displayed.
        anyAggressive = False

        #aggressive enemies first, then neutral, then passive
        for npc in room["npcs"]:
            if npc.aggression == "aggressive":
                print("A "+ npc.name +" blocks your path!")
                print("-"+npc.description+"\n")
                anyAggressive = True
        #aggressive enemies first, then neutral, then passive
        for npc in room["npcs"]:
            if npc.aggression == "neutral" and anyAggressive == False:
                print("You encounter a "+ npc.name +"!")
                print("-"+npc.description+"\n")
        #aggressive enemies first, then neutral, then passive
        for npc in room["npcs"]:
            if npc.aggression == "passive" and anyAggressive == False:
                print("You encounter a "+ npc.name +"!")
                print("-"+npc.description+"\n")


def print_room(room):
    
    print()
    print(room["name"].upper())
    print()

    # Display room description
    print(room["description"])
    print()

    print_room_items(room)
    print_npcs(room)

def exit_leads_to(exits, direction):
  
    return floors[exits[direction]]["name"]


def print_exit(direction, leads_to):
   
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, room_npcs, inv_items):
    
    print("You can:")
    
    # Iterate over available exits
    lockedExits = []
    if "locked" in current_room.keys():
        lockedExits = current_room["locked"]
    for direction in exits:

        if direction not in lockedExits:
            # Print the exit name and where it leads to
            print_exit(direction, exit_leads_to(exits, direction))


    #prints a statement for each item in the room
    for item in room_items:

        print("TAKE "+item["id"].upper() + " to take " + item["name"])

    #print a statement for each friendly npc in the room
    for npc in room_npcs:
        if npc.aggression=="passive" or npc.aggression=="neutral":
            print("SPEAK "+npc.id.upper() + " to speak to " + npc.name)

    #open map command
    if current_room["Floor"] != 0:
        print("OPEN MAP to take a look at your map")
    
    #option to open inventory
    print("OPEN INV to take a look at your inventory")
    
    if Dialog==True:
        print("Stop Dialog to stop dialog")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    lockedExits = []
    if "locked" in current_room.keys():
        lockedExits = current_room["locked"]
    print(chosen_exit)
    return (chosen_exit in exits and chosen_exit not in lockedExits)


def execute_go(direction):

    global current_room, previous_room, message, Played

    #checks if the chosen exit is valid
    if is_valid_exit(current_room["exits"], direction) == True:

        #store the previously visited room
        previous_room = current_room

        #updates the current room to the new room chosen by the user
        current_room = floors[current_room["exits"][direction]]
        Played=False

        message.append("You travel "+direction)


    #if exit is invalid display an error
    else:
        message.append("You cannot go '"+direction+"'.")


def execute_take(item_id):
 
    global message

    item_found = False

    #loop through all items in the room
    for item in current_room["items"]:

        #if the id of the current itemand the item selected by the player match,
        if item_id == item["id"]:
            item_found = True
            
            #calculate inventory weight
            weight = 0
            for player_item in inventory:
                weight = weight + player_item["weight"]

            #if item will fit in inventory
            if item["weight"] + weight <= weight_limit:
        
                #add to inventory and remove from the current room
                inventory.append(item)
                current_room["items"].remove(item)

                message.append(item["name"]+ " added to your inventory")
                
                #break to stop duplicate objects being picked up
                break

            else:
                message.append("Item is too heavy. Drop something from your inventory.")

    #if no item matches, print an error
    if item_found == False:
        message.append("You cannot take '"+item_id+"'.")
        
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    global message

    item_dropped = False

    #loop through items in inventory
    for item in inventory:

        #if the item entered by the user matches an item in inventory
        if item_id == item["id"]:

            #remove item from inventory and add it to the room
            inventory.remove(item)
            current_room["items"].append(item)
            item_dropped = True

            message.append(item["name"]+ " dropped from your inventory")

            #break to stop duplicate items being dropped
            break

    #if no item matches, print an error
    if item_dropped == False:
        message.append("You cannot drop '"+item_id+"'.")
    

def execute_command(command):
    global Dialog
    global message
    

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            message.append("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            message.append("Take what?")

    #command to open inventory
    elif command[0] == "open":
        if len(command) > 1:
            if command[1] == "inv":
                message.append("You open your inventory")
                print_inventory_items(inventory)
            elif command[1] == "map" and current_room["Floor"] != 0:
                message.append("You open your map")
                print_map()
            else:
                message.append("You cannot open '"+command[1]+"'.")
        else:
            message.append("Open what?")
    
    #command to speak to an npc
    elif command[0] == "speak":
        if len(command) > 1:
            for npc in current_room["npcs"]:
                if npc.aggression == "passive":
                    if command[1] == npc.id:
                        message.append("You approach "+npc.name)
                        
                        #if npc has diologue options
                        if npc.speech != "":
                            for line in npc.speech["diologue"]:
                                message.append(line)
                                print_lines()
                                input("> ")
                            speech = ""
                        

                        
                        
                        speak_merchant(inventory, npc)
                elif npc.aggression == "neutral":
                    if command[1] == npc.id:
                        message.append("You approach "+npc.name)
                        speak_enemy(npc)
                        
            else:
                message.append("You cannot speak to '"+command[1]+"'.")
        else:
            message.append("Speak to who?")

    

    else:
        message.append("This makes no sense.")


   

def menu(exits, room_items, room_npcs, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, room_npcs, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return floors[exits[direction]]

def boss_fight(npc):
    global Dialog
    global in_combat
    global FinishedFinalBossDialog
    in_combat = False
    if FinishedFinalBossDialog==False:
        time.sleep(2)
        print("You approach " + npc.name+"...")
        input("> ")
        print(FinishedFinalBossDialog)
    if FinishedFinalBossDialog==True:
        in_combat = True
        combat(npc)
    if (Dialog==True or Dialog == False) and FinishedFinalBossDialog==False:
        print("""\nYou: 'Hans!'""")
        input("> ")
        print("""Hans: 'Oh! Dante! what an absolute pleasure to see you. I see you were able to find your way here, took you way longer
than I expected but I'm so glad you're here, I was so bored of doing all this on my own.'""")
        input("> ")
        print("""You: 'Hans, what- what is this? I thought you were in trouble, you were missing you-'""")
        input("> ")
        print("Hans: 'Oh don't be worried silly, I've just been here for the past 3 days. I needed to finish my project.'")
        input("> ")
        print("You: 'Project? project- This is your project? The one you were so excited to show me? You are killing people Hans!'")
        input("> ")
        print("""Hans: 'I am not killing them! I am not! I am creating an army, Dante, and army that both of us will lead, an army that can never
be defeated!.""")
        input("> ")
        print("We will take over the world together! Join me brother dearest, together we will be unstoppable.'")
        print("\nYou can:")
        print("JOIN to join your brother and end the game.")
        print("FIGHT to oppose him.")

        user_input = input("> ")
        user_input = normalise_input(user_input)

        if user_input[0] == "fight" and FinishedFinalBossDialog==False:
            print("\n\nYou: 'No.'")
            input("> ")
            print("Hans: 'No? did you just say no?'")
            input("> ")
            print("You: 'I will not support you in this Hans, this is wrong and it always will be. I will do everything in my power to stop you'")
            input("> ")
            print("Hans: 'Well If you won't support me, then you will become one of them too.'")
            input("> ")
            
            
            time.sleep(3)
            in_combat = True
            FinishedFinalBossDialog=True
            combat(npc)
        elif user_input[0] == "join":

            print("""You: 'I will join you, my brother.'

Hans: 'I knew you will, I just knew it! oh why didn't I just tell you sooner? It would have taken a lot less time and it would've been so much more fun. It's ok it's ok, now that you are with me, there is nothing that can stop me. """)
            print("\n You joined hands with Hans and together you took over the world. \n")
            FinishedFinalBossDialog=True
            sys.exit()
        else:
            print("Can't do that.")
            FinishedFinalBossDialog=True
            boss_fight(npc)

# This is the entry point of our program
def main():
    global message
    global in_combat
    global Played
    message = ["Welcome to Beneath the Bones.",
               "Press the ENTER key to start a new game."]

    print_lines()
    input("> ")
    message.append("You sit inside your home and think of your missing brother, the news blares in the background.")

    
    
    # Main game loop
    while True:
        print_lines()
        
        # Display game status (room description, inventory etc.)
        print_room(current_room)

        #check if any npcs in the current room are aggressive
        in_combat = False
        for npc in current_room["npcs"]:
            if npc.aggression == "aggressive":
                #trigger an ambush
                in_combat = True

                combat(npc)
            elif npc.aggression == "boss":
                boss_fight(npc)
        if health <= 0:
            death()
        
        
        elif in_combat == False:        
        # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["items"],
                       current_room["npcs"], inventory)

        # Execute the player's command
            execute_command(command)
            
            


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
