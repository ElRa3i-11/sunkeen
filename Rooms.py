from entities import Enemy
slime1 = Enemy("Slime",40,5,2,"nothing",100,40)
slime2 = Enemy("Slime",40,5,2,"nothing",100,40)
manticore = Enemy("Manticore",100,20,15,"nothing",500,100)
minotaur = Enemy("Minotaur",200,10,5,"nothing",200,200)
ROOMS = {
    "starting room":{
        "name" : "starting room",
        "enemy" : None,
        "loot" : {
            "gold" : 10,
            "healing potion":1,
        },
        "exit" : {
            "q" : "Hallway",
            "z" : None,
            "s":None,
            "d":None
        }
    },
    "Hallway":{
        "name" : "Hallway (section 1)",
        "enemy" : None,
        "loot" : {
            "gold" : 0,
            "healing potion":0,
        },
        "exit" : {
            "q" :"Hallway2",
            "z" : "Treasury room" ,
            "s":"Ferdinand room",
            "d":"starting room"
        }
    },
    "Hallway2":{
        "name" : "Hallway (section2)",
        "enemy" : None,
        "loot" : {
            "gold" : 0,
            "healing potion":0,
        },
        "exit" : {
            "q" :"Hallway3",
            "z" : "Hallway4" ,
            "s":None,
            "d":"Hallway",
        }
    },
    "Hallway3":{
        "name" : "Hallway (section3)",
        "enemy" : None,

        "loot" : {
            "gold" : 0,
            "healing potion":0,
        },
        "exit" : {
            "q":None,
            "z" : None,
            "s":"Minotaur room",
            "d":"Hallway2",
        }

    },
    "Hallway4":{
        "name" : "Hallway (upper_section)",
        "enemy" : None,
        "loot" : {
            "gold" : 0,
            "healing potion":0,
        },
        "exit" : {
            "q":"Manticore room",
            "z" : None ,
            "s":"Hallway2",
            "d":None,
        }
    },
    "Ferdinand room":{
        "name" : "Ferdinand room",
        "enemy" : slime1,
        "loot" : {
            "gold" : 100,
            "healing potion":1,
        },
        "exit" : {
            "q":None,
            "z" : "Hallway" ,
            "s":None,
            "d":None
        }
    },
    "Treasury room":{
        "name" : "Treasury room",
        "enemy" : slime2,
        "loot" : {
            "gold" : 50,
            "healing potion":1,
        },
        "exit" : {
            "q":None,
            "z" : None ,
            "s":"Hallway",
            "d":None
        }
    },
    "Minotaur room":{
        "name" : "Minotaur Room",
        "enemy" : minotaur,
        "loot" : {
            "gold" : 300,
            "healing potion":0,
        },
        "exit" : {
            "q":None,
            "z" : "Hallway3" ,
            "s":None,
            "d":None
        }

    },
    "Manticore room":{
        "name" : "Manticore Room",
        "enemy" : manticore,
        "loot" : {
            "gold" : 200,
            "healing potion":1,
        },
        "exit" : {
            "q":"Hallway4",
            "z" : None ,
            "s":None,
            "d":None
        }

    }
}
current_room_name = ROOMS["starting room"]["name"]