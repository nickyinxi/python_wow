from main import Character, Monster


def engage_combat(character: Character, monster: Monster, alive_monsters: dict):

    character.enter_combat()
    monster.enter_combat()

    while character.in_combat:
        # we start off the combat with the monster dealing the first blow
        monster_attack(monster, character)

        if not character.alive:
            alive_monsters[monster.name].leave_combat()
            print("{0} has slain character {1}".format(monster.name, character.name))

            character.prompt_revive()
            break

        command = input()

        while True:  # for commands that do not end the turn, like printing the stats or the possible commands
            if command == 'print stats':
                print("Character {0} is at {1}/{2} health.".format(character.name, character.health, character.max_health))
                print("Monster {0} is at {1}/{2} health".format(monster.name, monster.health, monster.max_health))
                command = input()
            else:
                break

        if command == 'attack':
            character_attack(character, monster)

        if not monster.alive:
            character.leave_combat()  # will exit the loop
            del alive_monsters[monster.name]  # removes the monster from the dictionary
            print("{0} has slain {1}".format(character.name, monster.name))



def monster_attack(attacker: Monster, victim: Character):
    attacker_swing = attacker.deal_damage()  # an integer representing the damage

    print("{0} attacks {1} for {2} damage!".format(attacker.name, victim.name, attacker_swing))

    victim.take_attack(attacker_swing)


def character_attack(attacker: Character, victim: Monster):
    attacker_swing = attacker.deal_damage()

    print("{0} attacks {1} for {2} damage!".format(attacker.name, victim.name, attacker_swing))

    victim.take_attack(attacker_swing)