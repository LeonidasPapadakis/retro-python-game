report1={
    "id": "report",

    "name": "Lab Report 1",

    "description" :"'These reports seem to document some sort of chemical trial.'",

    "value":50,

    "weight":1,

    "contents": """You read the lab report.

LAB REPORT 1: 
Date: September 21 2024
Test Subject: Rabbit
colour: White
weight:5 pounds

observation: Blood shot eyes, blood pours out of mouth. 
Test subject: Dead
Test: Failed """
}

report2={
    "id": "report",

    "name": "Lab Report 2",

    "description" :"'These reports seem to document some sort of chemical trial.'",

    "value":50,

    "weight":1,

    "contents": """You read the lab report.

LAB REPORT 2:
Date: September 28 2024
Test Subject: Cat
colour: Black 
weight: 8 pounds

Observation: Test subject shows signs of aggression and grows in size but soon blood pours out of it's eyes.

New Weight:14 pounds
Test Subject: Dead
Test: Failed"""
}

report3={
    "id": "report",

    "name": "Lab Report 3",

    "description" :"'These reports seem to document some sort of chemical trial.'",

    "value":50,

    "weight":1,

    "contents": """You read the lab report.

LAB REPORT 3:
Date: 5 October 2024
Test Subject: Tarantula
Colour: Black
weight: 85 grams

observation: Test subject shows signs of aggression and increases in size significantly, it partially obeys commands and manages to survive. 

New Weight: 2 kg
Test Subject: Alive
Test: Partial Success"""
}

report4={
    "id": "report",

    "name": "Lab Report 4",

    "description" :"'These reports seem to document some sort of chemical trial.'",

    "value":50,

    "weight":1,

    "contents": """You read the lab report.

LAB REPORT 4:
Date: 12 October 2024
Test Subject: Human
Weight: 75 kg
Height: 5'11

Observation: Test Subject shows signs of aggression and increases significantly in size. It obeys commands better than the previous test subject, gains twice the strength of an average human and manages to survive. 

New Weight: 95 kg 
New Height: 6'6
Test Subject: Alive
Test: Partial success"""
}


item_cleaver = {
    "id": "cleaver",

    "name": "Butcher's Cleaver",

    "description":
    "A large rusted meat cleaver, stained with the blood of its most recent victim. ",

    "damage": 60,

    "value": 100,

    "weight": 25,

}

item_axe = {
    "id": "axe",

    "name": "Genetic-Splicing Axe",

    "description":
    "This axe doesn't just pierce flesh. It pierces the very fibre of what makes a person unique. ",

    "damage": 100,

    "value": 500,

    "weight": 50,


}

item_staff = {
    "id": "staff",

    "name": "Staff of the Flesh Witch",

    "description":
    "A staff carved from the bone of a great beast. It was made by a dark force, but you can put it to good use.",

    "damage": 88,

    "value": 150,

    "weight": 20,

}

item_sword = {
    "id": "sword",

    "name": "Caver's Sword",

    "description":
    "A short blade, scarred from use.",

    "damage": 50,

    "value": 80,

    "weight": 30,

}


item_stick = {
    "id": "stick",

    "name": "Stick",

    "description":
    """"A long, sharp looking stick. This might be good to defend
against creepy crawlys!""",

    "damage": 10,

    "value": 5,

    "weight": 20,
}

item_club = {
    "id": "club",

    "name": "Fungal Club",

    "description":
    """A large mushroom with a thick, heavy head. This will make
a good blunt weapon.
""",

    "damage": 30,

    "value": 20,

    "weight": 40,

}



Small_healing_potion={
    "id": "brew",

    "name": "Herbal Brew",

    "description" :
"""A warm herbal remedy made by the cave dwellers.
(+20 Health)""",
    
    "value":15,

    "effects":{"health":20},

    "weight":10,
}


Medium_healing_potion={
    "id": "tube",

    "name": "Test Tube",

    "description" :"""A small test tube filled with a fresh smelling liquid.
(+40 Health)""",

    "value":25,

    "effects":{"health":40},

    "weight":20,
}

large_healing_potion={
    "id": "tonic",

    "name": "Medical Tonic",

    "description" :"""A large glass bottle full of a lovely red goo.
(+80 Health)""",

    "value":40,

    "effects":{"health":80},

    "weight":30,
}

brothers_journal={
    "id": "journal",

    "name": "journal",

    "description" :"'This is his journal, he would never let me read it if he was here. Good thing he's not here.'",

    "value":10,

    "weight":5,

    "contents": """You read the most recent entry.

October 21, 2024 \n \n'Dear Diary, today has been great, I made so much progress on this project I have been working on and I can't wait to show it to my brother,
I know for a fact that he will absolutely love it. I think I might go visit the cave today as well, remember?
the same cave that dante and I used to go to when we were kids, oh how much it would upset our mum when we went,
she used to be absolutely pissed but it was our safe space, our second home. 
Anyways, I'll keep you updated on my project!'

A strange feeling now pulls you to the cave...
""",

    "exits": {"Brothers Room":"south"}
}


rabbit={
    "id": "rabbit",

    "name": "Dead Rabbit",

    "description" :"Looks diseased, definately not dinner!",

    "value":30,

    "weight":10}





iron_rock={
    "id": "iron",

    "name": "Iron Rock",

    "description" :"A chunk of iron.",

    "value":15,

    "weight":5,


}

gold_rock={
    "id": "gold",

    "name": "Gold Rock",

    "description" :"A glistening chunk of gold!",

    "value":25,

    "weight":5,
}

diamond_rock={
    "id": "diamond",

    "name": "Diamond",

    "description" :"A huge, crystal clear diamond!",

    "value":50,

    "weight":5,

}

iron_sword= {
    "id": "ironsword",

    "name": "iron sword",

    "description":
    "Just a test item",

    "damage": 40,

    "value": 45,

    "weight": 20
}


double_damage_potion={
    "id":"might",

    "name" : "Might Syrum",

    "description":
    """This firey goop enrages you from its scent alone.
(x2 Damage multiplier)""",

    "effects": {"damage":2},

    "value": 45,

    "weight": 10,

}
Paralysis_Potion={
    "id":"potion",

    "name" : "Weakening Potion",

    "description":
    "A stinking, paralysing liquid. You do not want to spill this.\n(Halves enemies attack for one turn)",

    "damage": 1,

    "value": 40,

    "weight": 10,
}
