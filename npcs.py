from items import *

class Npcs():
    def __init__(self,name,description,aggression,mana=0,items = [],damage=50,health=100,id="", speech = ""):
        self.name=name
        self.description=description
        self.damage=damage
        self.health=health
        self.items=items
        self.aggression=aggression
        self.mana=mana
        self.id=id
        self.speech=speech
#need to add sound effect for every  instance

monster=Npcs(name="Monster",description="description",mana=15,damage=50,health=100,items=[large_healing_potion],aggression="aggressive")
spider=Npcs(name="Spider",description="description",damage=50,mana=20,health=120,items=[iron_rock,Medium_healing_potion],aggression="aggressive")

merchant1=Npcs(name="Cave Dweller",
               id = "dweller",
               description="""A small old lady perched on a rock with a basket of goods.
She smiles and waves you over.""",

               speech=


{"diologue":["""You - 'Oh god! Thank god I met you, you won't believe what i just saw. A giant rabbit! It-It was- there is something very wrong here!'""",

"""Cave Dweller - 'You are dante. dante, dante, dante, dante. The brother. I am a cave dweller. My people and I are here to guide you.'""",

"""You - 'What exactly is happening here? Where is my brother?'""",

"""Cave Dweller -  'I cannot say much to you, Dante, I can only offer you a few items. You may choose to take anything you want but
remember you always need to give something to me in return.""",

"""You - 'What does this mean? what sort of a sick joke is this?' """,

"""Cave Dweller - Go fetch that rabbit and I will trade you it for a couple of my own homemade brews"""]},
               health=100,
               items=[Small_healing_potion, Small_healing_potion],
               aggression="passive")


merchant2=Npcs(name="Cave Dweller",
               id = "dweller",
               speech=


{"diologue":["""Cave Dweller - 'Welcome down Dante. Do you have things to sell? I have plenty to buy.'""",

"""You - 'You know me? Where can I find my brother'""",

"""Cave Dweller -  'Do not worry, he will be found. Would you like some tools to help guide you on your journey.'""",

"""You - 'Show me what you have.' """]},

               description="""A strange looking man huddled in the corner with a large sack.

Cave Dweller - 'Please, approach and see my wares.'""",
               health=100,
               items=[Small_healing_potion,Medium_healing_potion,Medium_healing_potion, large_healing_potion,item_sword, double_damage_potion],
               aggression="passive")



merchant3=Npcs(name="Scientist",
               id = "scientist",
               speech=


{"diologue":["""You - 'Greetings, do you know of my brother? Where can I find him?'""",

"""Scientist - 'He is not far now Dante. You can feel it in your bones can't you. He's close.'""",

"""You - 'Fine, let me see your stock.' """]},

               description="""A professional looking lady in a white jacket. She seems to fit right into this laboratory.

Scientist - 'Come, see what I have brewed up.'""",

               health=100,
               items=[Medium_healing_potion, large_healing_potion,large_healing_potion,double_damage_potion,double_damage_potion],
               aggression="passive")

merchant4=Npcs(name="Head Mixer",
               id = "mixer",
               speech=


{"diologue":["""You - 'Who are you? The witch told me my brother is nearby.'""",

"""Head Mixer - 'Yes your brother! I know of him but I'm afraid I won't say more. I sense you will be reunited soon.'""",

"""You - 'We will be I'm sure of it. Go on then show me your stock.' """]},

               description="""A small man with a hunched back. He wears a pair of gold rimmed glasses.

Head Mixer - 'Ah Dante. I have been expecting you. Come buy from me.'""",
               health=100,
               items=[item_axe,Medium_healing_potion, large_healing_potion,large_healing_potion,double_damage_potion,double_damage_potion],
               aggression="passive")


rabbit1= Npcs(name="Rabid Rabbit",
              description =
              """This is no ordinary rabbit. This rabbit seems hungry for blood!""",
              damage = 10,
              items = [rabbit],
              health = 20,
              aggression = "aggressive",
              mana=7
              )

rat1 = Npcs(name="Mutant Rat",
              description =
              """A snarling rodent pumped up to the size of a dog, a red foam
drips from its mouth. Its beady eyes glow like candles
in the dark tunnel.""",
              damage = 25,
              items = [double_damage_potion],
              health = 50,
              aggression = "aggressive",
              mana=27
              )

bear= Npcs(name="Bear",
              description =
              """This is no ordinary Bear. This Bear seems hungry for blood!""",
              damage = 40,
              health = 120,
              items=[iron_rock, double_damage_potion],
              aggression = "aggressive",
              mana=29
              )

madman= Npcs(name="Mad Man Mikey",
             id = "mikey",
              description =
              """A skinny man dressed in rags and holding a silver spoon. He stands blocking
a passage to the east. His beady eyes stare at you from across the room. He grins and
beckons you over.

Mad Man Mikey - 'Approach me boy, play a game with me.'""",
              damage = 30,
              health = 100,
              items=[large_healing_potion],
              aggression = "neutral",
             speech={
                 "diologue": ["""Mad Man Mikey - 'Come closer, I dont bite...'""",
                              """Mad Man Mikey - 'Much!'""",
                              """You - 'I mean you no harm. I would like to pass through here please.'""",
                              """Mad Man Mikey - 'Why such a hurry? Lets chat.'"""],
                 "questions": ["""Answer my question correctly and I will let you can pass safely! What comes once in a minute, twice in a moment,\nbut never in a thousand years?""",
                               "m","Wrong! I'll give you two more guesses and ask you again. What comes\nonce in a minute, twice in a moment, but never in a thousand years?","m",
                               """Wrong again! Last chance to leave this cave in a solid form!\nI ask you for a final time, what comes once in a minute, twice in a
moment, but never in a thousand years?""","m"],
                 "attack": "You fool, wrong again! Now get on my spoon, dinner!",
                 "pass": "Oo a clever one! I am dissapointed but very well, you shall pass. \nI welcome you into trade too.",
                 "exits": ["east"]
              })

bandit= Npcs(name="Bandit Bill",
             id = "bill",
              description =
              """A big beast of a man outfitted in gold from head to toe. He stands blocking the exit south.

Bandit Bill - 'Oi you, get over here.'""",
              damage = 25,
              health = 220,
              items=[large_healing_potion],
              aggression = "neutral",
             speech={
                 "diologue": ["""Bandit Bill - 'Oi you! If ya wanna get through this here passageway, yer gonna have to prove you've got half a brain ok?'""",
                              """You - 'Fine, ask me and get it over with.'"""],
                 "questions": ["""I'll give ya three guesses. What can't be used, till its broken?""",
                               "egg","Nope! Two more guesses! What can't be used till its broken?","egg",
                               """Wrong again! What can't be used till its broken?""","egg"],
                 "attack": "Ha ha ha you are wrong! Now give me yer gold!",
                 "pass": "Very good! Go on then off you go. Stick around and chat if you wanna trade, yeah?",
                 "exits": ["south" ]})



witch= Npcs(name="Flesh Witch",
             id = "witch",
              description =
              """Hunched over by the east passage, a witch watches you and shows her brown teeth. Her outfit seems to be sewn from human skin.
She holds a glowing red staff in one hand and beckons you closer with the other...""",
              damage = 35,
              health = 220,
              items=[large_healing_potion,item_staff, diamond_rock],
              aggression = "neutral",
             speech={
                 "diologue": ["""You - 'Witch! Where is my brother? Where have you taken him?'""",
                              """Flesh Witch - 'HA-HA-HA-HA-HA!'""",
                              """You - 'Let me through this passage or I will fight my way through!'""",
                              """Flesh Witch - 'Answer my riddle and you will find your brother not far beyond this door!'""",
                              """You - 'Fine, I will pass whatever test you have for me!'""",
                              """Flesh Witch - 'HA-HA-HA-HA-HA! Not in three guesses and not in a million years!'"""],
                "questions": ["""What word starts with an e, ends with an e, and has one letter in it?""",
                               "envelope","HA-HA-HA-HA-HA! One finger down! What word starts with an e, ends with an e, and has one letter in it?","envelope",
                               """HA-HA-HA-HA-HA! You're not very good at this but you'll be great in my stew! HA-HA-HA-HA-HA! \nWhat word starts with an e, ends with an e, and has one letter in it?""","envelope"],
                 
                 "attack": "MM-MM-MM! In the couldren you go! HA-HA-HA-HA-HA!",
                 "pass": "Oh good very good! I stand aside for you Dante, and welcome you to trade with me.",
                 "exits": ["east" ]})



rabbit2= Npcs(name="Mother Bunny",
              description =
              """This rabbit is mutated to the size of a dog.
And it wants vengance...""",
              damage = 25,
              items = [rabbit, double_damage_potion],
              health = 50,
              aggression = "aggressive",
              mana=7
              )

butcher= Npcs(name="The Butcher",
              description =
              """A tall masked figure in a bloody apron. He holds a rusty cleaver. He seems enraged by the sight of you!""",
              damage = 33,
              items = [double_damage_potion, item_cleaver],
              health = 150,
              aggression = "aggressive",
              mana=7
              )

bull= Npcs(name="The Bull",
              description =
              """A monster leaps from the shadows. It has the head of a bull with the body of a man. It towers over you and lets out
a piercing shriek before lowering its horns and charging.""",
              damage = 20,
              items = [double_damage_potion, double_damage_potion, double_damage_potion, large_healing_potion],
              health = 400,
              aggression = "aggressive",
              mana=7
              )

mutant= Npcs(name="Mutant",
              description =
              """This creature looks barely human. It cries out in pain and pulls at its skin.""",
              damage = 30,
              items = [double_damage_potion, double_damage_potion, large_healing_potion, diamond_rock],
              health = 400,
              aggression = "aggressive",
              mana=7
              )

mutant2= Npcs(name="Mutated human",
              description =
              """This man foams from the mouth and is trapped in a state of aggression, as if he was rabbid. He blocks your path.""",
              damage = 25,
              items = [double_damage_potion],
              health = 160,
              aggression = "aggressive",
              mana=7
              )

boss= Npcs(name="Hans",
             id = "hans",
              description =
              """""",
              damage = 25,
              health = 1000,
              items=[],
              aggression = "boss",
              mana=50
              )

npcs={
    "merchant1":[merchant1,{"health":100}],
    "merchant2":merchant2,
    "merchant3":merchant3,
    "monster":[monster,{"health":100}],
    "spider":[spider,{"health":120}],
    "Rabid Rabbit":[rabbit1,{"health":20}],
    "bear":[bear,{"health":120}],
    "madman":madman,
    "Mutant Rat":[rat1,{"health":50}]
}
