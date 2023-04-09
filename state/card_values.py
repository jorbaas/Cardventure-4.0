import random

##### HUMAN CARDS #####

H_1 = {'name': 'basic human',
       'type': 'human',
       'id': 0,
       'name_image': 'office_human_image.png',
       'name_card': 'human_template.png',
       'attack': 3,
       'defense': 3,
       'effect': None,
       'description': "Like you, pretty basic,\nbut different nonetheless."
       }

H_2 = {'name': 'chad human',
       'type': 'human',
       'id': 0,
       'name_image': 'chad_human_image.png',
       'name_card': 'human_template.png',
       'attack': 4,
       'defense': 4,
       'effect': None,
       'description': "Such a chad, that he just decided to become one."
       }

H_3 = {'name': 'Lonely tank',
       'type': 'human',
       'id': 0,
       'name_image': 'tank_human_image.png',
       'name_card': 'human_template.png',
       'attack': 8,
       'defense': 8,
       'effect': None,
       'description': "Doing tank stuff."
       }

H_4 = {'name': 'Mechman',
       'type': 'human',
       'id': 0,
       'name_image': 'mechsuit_human_image.png',
       'name_card': 'human_template.png',
       'attack': 6,
       'defense': 5,
       'effect': None,
       'description': "very strong but also strong."
       }

##### BEAST CARDS #####

B_1 = {'name': 'rat',
       'type': 'beast',
       'id': 0,
       'name_image': 'rat_beast_image.png',
       'name_card': 'beast_template.png',
       'attack': 2,
       'defense': 2,
       'effect': None,
       'description': "A rat, but a tad stronger,\nis it an ...?"
       }

B_2 = {'name': 'boar',
       'type': 'beast',
       'id': 0,
       'name_image': 'boar_beast_image.png',
       'name_card': 'beast_template.png',
       'attack': 3,
       'defense': 4,
       'effect': None,
       'description': "Sniffs around, but is also dangerous"
       }

B_3 = {'name': 'Jacked Beetle',
       'type': 'beast',
       'id': 0,
       'name_image': 'beetle_beast_image.png',
       'name_card': 'beast_template.png',
       'attack': 3,
       'defense': 5,
       'effect': None,
       'description': "Rises once in 100 years from the ground"
       }

B_4 = {'name': '50 year old snail',
       'type': 'beast',
       'id': 0,
       'name_image': 'snail_beast_image.png',
       'name_card': 'beast_template.png',
       'attack': 0,
       'defense': 6,
       'effect': None,
       'description': "with his slime and dirt he creates concreate to make his stone shell with"
       }



##### SAINT CARDS #####

S_1 = {'name': 'basic saint',
       'type': 'saint',
       'id': 0,
       'name_image': 'basic_saint_image.png',
       'name_card': 'saint_template.png',
       'attack': 2,
       'defense': 4,
       'effect': None,
       'description': "Closer to God\nthan you likely ever will be."
       }

S_2 = {'name': 'happy fat monk',
       'type': 'saint',
       'id': 0,
       'name_image': 'happy_monk_saint_image.png',
       'name_card': 'saint_template.png',
       'attack': 0,
       'defense': 5,
       'effect': None,
       'description': "Eats and meditates, in that order."
       }

S_3 = {'name': 'Holy rubber duck',
       'type': 'saint',
       'id': 0,
       'name_image': 'duck_saint_image.png',
       'name_card': 'saint_template.png',
       'attack': 0,
       'defense': 2,
       'effect': None,
       'description': "Turns the water he floats in\n into holy water."
       }


##### DEMON CARDS #####

D_1 = {'name': 'goat',
       'type': 'demon',
       'id': 0,
       'name_image': 'goat_demon_image.png',
       'name_card': 'demon_template.png',
       'attack': 4,
       'defense': 2,
       'effect': None,
       'description': "A Goat.\nPortal to many dimensions"
       }

D_2 = {'name': 'something is under there',
       'type': 'demon',
       'id': 0,
       'name_image': 'bed_demon_image.png',
       'name_card': 'demon_template.png',
       'attack': 5,
       'defense': 0,
       'effect': None,
       'description': "Your worst fantasies from when you were 6."
       }

D_3 = {'name': 'Visitor',
       'type': 'demon',
       'id': 0,
       'name_image': 'alien_demon_image.png',
       'name_card': 'demon_template.png',
       'attack': 6,
       'defense': 2,
       'effect': None,
       'description': "Just when you want ot grab a sandwich"
       }



ALL_CARDS = [H_1, H_2, H_3, H_4,
             B_1, B_2, B_3, B_4,
             S_1, S_2,
             D_1, D_2, D_3
             ]

TEST_DECK = [H_1, H_2, H_3, H_4,H_1, H_2, H_3, H_4,
             B_1, B_2, B_3, B_4,
             S_1, S_2, S_3, S_3, S_3, S_3,
             D_1, D_2, D_3,
             B_1, B_2, B_3, B_4,
             S_1, S_2,
             D_1, D_2, D_3, H_1, H_2, H_3, H_4,
             B_1, B_2, B_3, B_4,
             S_1, S_2,
             D_1, D_2, D_3, H_1, H_2, H_3, H_4,
             B_1, B_2, B_3, B_4,
             S_1, S_2,
             D_1, D_2, D_3
             ]