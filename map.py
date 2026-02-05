from items import *
from npcs import *
#from rooms_map import *

#changed rooms to floors, rooms dictionary is now floors , exit key in each floor dictionary (floor_1 etc) now has one value which 
# is the floor above going to change so that each floor dictionary has exits which are rooms in the floor , travel through rooms in the floor
#in order to get to next floor , description of each floor will be added



house_0 = {
    "name": "Living Room",

    "description": """NEWS: 'Two more people have gone missing in the past 24 hours,
      the police are not releasing any information on the matter.
Is there a serial killer on the loose? or a mass kidnapping? I personally think-'

'3 days, 72 hours. My brother has been missing, no one knows where he is, is he dead?
is he alive? we know nothing. I check my phone everyday, every second for a message from him,
omething that would tell me that he's ok but I get nothing. I can't the shake the terrible
thoughts away, the possibilities of what could have happened, i wish i could just get to him
and bring him home.'

(A sad urge pulls you upstairs to your brother's room...)""",

    "exits": {"upstairs": "house1"},

    "items": [],

    "npcs": [],

    "enemies": [],

    "Floor" : 0

    }

house_1 = {
    "name": "Brothers Room",

    "description": """Nothing is out of place. The room is clean and organised, just how Hans kept it. Your eyes are drawn
to a thick leather covered book on the desk.""",

    "exits": {"south": "room1"},

    "locked": ["south"],

    "items": [brothers_journal],

    "npcs": [],

    "Floor" : 0

    }

room_1 = {
    "name": "Level 1: Cave Opening",

    "description": """You have just entered the cave, everything still bright from the sunlight. The moment you step in a rock
falls down from the roof and you leap to avoid it. The rock now blocks the way out. You see your brothers watch on the
floor and a path continuing deeper...""",

    "exits": {"west": "room2"},

    "items": [item_stick],

    "npcs": [],

    "Floor" : 1

}

room_2 = {
    "name": "Echoing Cavern",

    "description":"""A melancholy symphony of music and quiet fills the dimly lighted space. 
    The stone walls echoed with every muttered secret. .You hear a growl from the right side of the room and turn around to find..... """,

    "exits":  {"west": "room3", "east": "room1"},

    "items": [],

    "npcs": [rabbit1],

    "Floor" : 1
}

room_3 = {
    "name": "Glimmering Pools",

    "description":
    """Walking in, you're taken aback by the sight in front of you. Under the gentle glow of bioluminescent mushrooms,
crystalline waters shimmer, creating captivating reflections on the rugged stone walls. """,

    "exits": {"east": "room2", "west": "room4"},

    "items": [],

    "npcs": [merchant1],

    "Floor" : 1
}

room_4 = {
    "name": "Fungal Alcove",

    "description":
    """A damp fungal smell greets you as you enter a room with strange mushrooms growing everywhere. Glowing mushrooms
dot the ground, lighting up the room with a blue mist. Thick stalks reach out from the walls like branches. A
dark, twisting passage leads to the south...""",

    "exits": {"east": "room3","south": "room5"},

    "items": [item_club],

    "npcs": [],

    "Floor" : 1
}

room_5 = {
    "name": "Twisted Tunnels",

    "description":
    """These cramped passages are only dimly lit with the occasional glowing mushroom. You cannot see very far down
the tunnel and you hear scuttling coming from the cave walls...""",

    "exits": {"north": "room4", "east": "room6"},

    "items": [],

    "npcs": [rat1],

    "Floor" : 1
}

room_6 = {
    "name": "The Wailing Hollow",

    "description":
    """The passage opens to a damp, gloomy cavern. There seems to be a rough den made from animal skins
and bones built in to a passage to the east.""",

    "exits": {"west": "room5","east": "room7"},

    "locked": ["east"],

    "items": [],

    "npcs": [madman],

    "Floor" : 1
}

room_7 = {
    "name": "The Gloomforge",

    "description":
    """ You enter a shadowy chamber filled with faint echos of clanging metal,
      where flickering torches cast eerie light on the rugged anvils and tools scattered throughout.""",

    "exits": {"south": "room8", "west": "room6"},

    "items": [gold_rock, Medium_healing_potion],

    "npcs": [],

    "Floor" : 1
}

room_8 = {
    "name": "Serpent’s Gorge",

    "description":
    """As you enter the room, you are met with a small, twisting passageway with walls that are covered in moist moss,
twisted like coiling snakes, and faintly lit by minerals. """,

    "exits": {"west": "room9", "north": "room7"},

    "items": [],

    "npcs": [rabbit2],

    "Floor" : 1
}

room_9 = {
    "name": "The Murmuring Depths ",

    "description":
    """you see a spacious cave filled with the gentle sound of dripping water,
where dark pools lay still beneath the soft glow of shimmering stones, creating a mysterious atmosphere. """,

    "exits": {"east": "room8", "down": "room10"},

    "items": [],

    "npcs": [bear],

    "Floor" : 1
}


room_10 = {
    "name": "Level 2: Fleshbane Hold",

    "description":
    """The air is heavy with the smell of wet dirt, and dark shadows lurk,
      hinting at the horrors that previously lived behind its walls. As you descend, you reach a chamber characterized by jagged rocks and a terrible atmosphere.  """,

    "exits": {"up": "room9", "west": "room11"},

    "items": [report1, large_healing_potion],

    "npcs": [],

    "Floor" : 2
}

room_11 = {
    "name": "Feeding Pens",

    "description":
    "Walking into the room you are hit by the smell of mold and dead meat; half eaten chickens lie on the cave floor.",

    "exits": {"east": "room10", "west": "room12"},

    "items": [],

    "npcs": [merchant2],

    "Floor" : 2
 
}

room_12 = {
    "name": "Bone Forge",

    "description":
    """entering the room you see many mutated skeletons propped up the cave walls.
They resemble human skeletons, however some bones are abnormally large and golden in colour.""",

    "exits": {"south": "room13", "east": "room11"},

    "items": [Small_healing_potion],

    "npcs": [],

    "Floor" : 2
}

room_13 = {
    "name": "The Butcher’s Arena",

    "description":
    "The room is dimly lit by flickering torches. In the center is a large stone slab covered in old dried blood. ",

    "exits": {"north": "room12", "east": "room14"},

    "items": [iron_rock, double_damage_potion],

    "npcs": [butcher],

    "Floor" : 2
}

room_14 = {
    "name": "The Rejection Wing",

    "description":
    """ Entering the room, you see cells lined up on both walls.
Walking closer you see plenty of animals but none of them respond to your presence, perhaps they are dead.""",

    "exits": {"west": "room13", "east": "room15"},

    "items": [report2, gold_rock],

    "npcs": [],

    "defeatedenemies" : [],

    "Floor" : 2
}

room_15 = {
    "name": "The Abomination Kennels",

    "description":
    "Dark, it's very dark. The echoes of pained groans and the smell of rot permeate the room as monsters writher in rusting cages. ",

    "exits": {"south": "room16", "west": "room14"},

    "items": [],

    "npcs": [bandit],

    "locked": ["south"],

    "Floor" : 2

}

room_16 = {
    "name": "The Molting Grounds",

    "description":
    "Entering the room you can see splashes of gold liquid on the cave grounds, you bend down to touch it, but something in your heart stops you. ",

    "exits": {"west": "room17", "north": "room15"},

    "items": [Medium_healing_potion, double_damage_potion],

    "npcs": [],

    "Floor" : 2
}

room_17 = {
    "name": "The Mutation Furnace",

    "description":
    """The hiss of steam and the brilliance of an odd pulsing light filled the dark, empty chamber.
      Looking down you see the same trail of golden liquid from the previous room. """,

    "exits": {"east": "room16", "down": "room18"},

    "items": [gold_rock],

    "npcs": [bull],

    "Floor" : 2
}

room_18 = {
    "name": "Level 3: Labratory",

    "description":
    """Walking down you enter a room that almost resembles a science lab. 
To the right are bubbling vials filled to the brim with green liquid, there are frenzied scribbles on the walls.""",

    "exits": {"up": "room17", "west": "room19"},

    "items": [],

    "npcs": [merchant3],

    "Floor" : 3
}

room_19 = {
    "name": "The Sculptor’s Workshop",

    "description":
    """you would've felt like you're not even in a cave if it wasn't for the stone walls because before you was a lab, 
an actual science lab. To the left there was all kinds of equipment, from beakers to test tubes. 
On the right was a chalkboard propped up against the wall full of chemical formulas.  """,

    "exits": {"west": "room20", "east": "room18"},

    "items": [report3],

    "npcs": [],

    "Floor" : 3
}

room_20 = {
    "name": "Mutagenic Pools",

    "description":
    """Under a roof of ragged rock, seething pools of shimmering liquid churn menacingly,
creating flickering shadows that suggest odd experiments being carried out underneath. 
The area is filled with the pungent smell of smoke and metal. """,

    "exits": {"south": "room21", "east": "room19"},

    "items": [Small_healing_potion],

    "npcs": [mutant],

    "Floor" : 3
}

room_21 = {
    "name": "The Monster Nursery",

    "description":
    """An eerie light is projected on the cave walls by the shadowy creatures who wiggle
amid nests of bright lighting eggs in this dimly lighted space that is filled with quiet, unnerving sounds. """,

    "exits": {"north": "room20", "east": "room22"},

    "items": [double_damage_potion],

    "npcs": [],

    "Floor" : 3
}

room_22 = {
    "name": "The Flesh Lab",

    "description":
    "Entering the room you are met with the smell of rotting flesh. A table on the right has a bunch of animal skin, perhaps used for testing. ",

    "exits": {"east": "room23", "west": "room21"},
    "locked": ["east"],

    "items": [],

    "npcs": [witch],

    "Floor" : 3

}

room_23 = {
    "name": "The Cocoon Room",

    "description":
    """A really odd sight greets you as soon as you enter the room. Luminescent pods, 
each throbbing softly with an enigmatic glow, hang from the ceiling of the enclave, which is covered with silky treads. """,

    "exits": {"south": "room24", "west": "room22"},

    "items": [large_healing_potion,report4],

    "npcs": [mutant2],
    
    "Floor" : 3
}

room_24 = {
    "name": "Genetic Splicing Lab",

    "description":
    """The room is a stark  chamber filled with illuminated vials and complicated devices.
On a shelf you can see body parts preserved in water in a jar. The air hums with the vow of experimentation in every corner. """,

    "exits": {"north": "room23", "west": "room25"},

    "items": [],

    "npcs": [merchant4],

    "Floor" : 3
}

room_25 = {
    "name": "The Puppet Master’s Theater",

    "description":
    """A chill sweeps through the dimly lit room, a flickering fluorescent lamp casts erratic shadows on the cracked walls.
      There is an ominous chalkboard with bizarre diagrams set to the right and in the center was Hans. 
      People always said that he had a child like wonder in his eyes, right now however, his eyes are alight with manic excitement.
      A stained lab coat and a syringe with golden liquid in his hand, Hans was bent over a person, ready to inject them with his creation. """,

    "exits": {"east": "room24"},

    "items": [],

    "npcs": [boss],

    "Floor" : 3
}


floors = {
    "house0": house_0,
    "house1": house_1,
    
    "room1": room_1,
    "room2": room_2,
    "room3": room_3,
    "room4": room_4,
    "room5": room_5,
    "room6": room_6,
    "room7": room_7,
    "room8": room_8,
    "room9": room_9,
    "room10": room_10,
    "room11": room_11,
    "room12": room_12,
    "room13": room_13,
    "room14": room_14,
    "room15": room_15,
    "room16": room_16,
    "room17": room_17,
    "room18": room_18,
    "room19": room_19,
    "room20": room_20,
    "room21": room_21,
    "room22": room_22,
    "room23": room_23,
    "room24": room_24,
    "room25": room_25,
    #"testRoom" : testRoom
}
