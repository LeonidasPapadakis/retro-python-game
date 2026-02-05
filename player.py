from items import *
from map import floors

FinishedFinalBossDialog=False
in_combat=False
inventory = []
coins = 0
weight_limit = 100
escape_chance = 75
health = 100
mana=0
Played=False

current_room = floors["house0"]
previous_room = floors["house0"]

max_health = 100
damage = 1.0

Dialog=False

#dictionary to save the games sate at a checkpoint
checkpoint = {
    "inventory" : "",

    "coins" : "",

    "weight_limit" : "",

    "escape_chance" : "",

    "health" : "",

    "current_room" : "",

    "previous_room" : "",

    "map" : "",

    "npcs" : ""
}
    
