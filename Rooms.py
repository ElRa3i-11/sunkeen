from entities import Enemy
slime1 = Enemy("Slime",40,5,2,"nothing",100,40)
slime2 = Enemy("Slime",40,5,2,"nothing",100,40)
manticore = Enemy("Manticore",100,20,15,"nothing",500,100)
minotaur = Enemy("Minotaur",200,10,5,"nothing",200,200)
ROOMS = {
    "starting room":{
        "name" : "starting room",
        "enemy" : None,
        "gold" : 10,
        "exit" : {
            "left" : "Hallway",
            "up" : None,
            "down":None,
            "right":None
        }

    },
    "Hallway":{
        "name" : "Hallway (section 1)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :"Hallway2",
            "up" : "Treasury room" ,
            "down":"Ferdinand room",
            "right":"starting room"
        }

    },
    "Hallway2":{
        "name" : "Hallway (section2)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :"Hallway3",
            "up" : "Hallway4" ,
            "down":None,
            "right":"Hallway",
        }

    },
    "Hallway3":{
        "name" : "Hallway (section3)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :None,
            "up" : None,
            "down":"Minotaur room",
            "right":"Hallway2",
        }

    },
    "Hallway4":{
        "name" : "Hallway (upper_section)",
        "enemy" : None,
        "gold" : 0,
        "exit" : {
            "left" :"Manticore room",
            "up" : None ,
            "down":"Hallway2",
            "right":None,
        }

    },

    "Ferdinand room":{
        "name" : "Ferdinand room",
        "enemy" : slime1,
        "gold" : 50,
        "exit" : {
            "left" :None,
            "up" : "Hallway" ,
            "down":None,
            "right":None
        }
    },
    "Treasury room":{
        "name" : "Treasury room",
        "enemy" : slime2,
        "gold" : 50,
        "exit" : {
            "left" :None,
            "up" : None ,
            "down":"Hallway",
            "right":None
        }

    },
    "Minotaur room":{
        "name" : "Minotaur Room",
        "enemy" : minotaur,
        "gold" : 300,
        "exit" : {
            "left" :None,
            "up" : None ,
            "down":"Hallway3",
            "right":None
        }

    },
    "Manticore room":{
        "name" : "Manticore Room",
        "enemy" : manticore,
        "gold" : 200,
        "exit" : {
            "left" :"Hallway4",
            "up" : None ,
            "down":None,
            "right":None
        }

    }
}
current_room_name = ROOMS["starting room"]["name"]