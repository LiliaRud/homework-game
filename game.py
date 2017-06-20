import random
from math import ceil

class Army:
    def __init__(self):
        self.max_units = 100
        self.group = []
    def __str__(self):
        group_str= []
        for i in self.group:
            group_str.append(str(i))
        return str(group_str)

    def player_choose(self):
        classes = {'Warrior': Warrior, 'Archer': Archer, 'Mage': Mage}
        check_max_unist = self.max_units
        while True:
            print('='*20)
            print('\nChoose class:(for exit type \'q\')\n')
            for cl in classes:
                print(cl)
            print('='*20)
            choose = input().capitalize()
            if choose.lower() == 'q':
                break
            elif choose in classes:
                units = int(input('Number of units:\n'))
                if units > check_max_unist:
                    print('\nYou can\'t take more then {0} units.\n'.format(self.max_units))
                else:
                    self.group.append(classes[choose](units))
                    check_max_unist = check_max_unist - units
                    classes.pop(choose)
            else:
                print('\nIncorrect instruction!\n')

            if len(classes) == 0:
                if self.group[0].units + self.group[1].units + self.group[2].units == self.max_units:
                    break
                elif self.group[0].units + self.group[1].units + self.group[2].units < self.max_units:
                    answ = input('Are you shure? Your Army can be weaker than enemy\'s Army (y or n) ')
                    if answ.lower() == 'y':
                        break
                    else:
                       continue
        return self.group

    def computer_choose(self):
        self.group.append(Warrior(random.randint(1, self.max_units)))
        self.group.append(Archer(random.randint(1, self.max_units - self.group[0].units)))
        self.group.append(Mage(self.max_units - self.group[0].units - self.group[1].units))
        random.shuffle(self.group)
        return self.group

    def game(self, other):
        pl_1 = self.group
        pl_2 = other.group
        while True:

            if pl_1[0].units <= 0:
                self.group.pop(0)

            if pl_2[0].units <= 0:
                other.group.pop(0)

            print(self, other)

            if len(self.group) == 0:
                print('Player 2 WON!')
                break

            if len(other.group) == 0:
                print('Player 1 WON!')
                break

            dmg_1_to_2 = pl_1[0].units * pl_1[0].dmg[pl_2[0].role]
            dmg_2_to_1 = pl_2[0].units * pl_2[0].dmg[pl_1[0].role]

            pl_1_hp = pl_1[0].units * pl_1[0].hp
            pl_2_hp = pl_2[0].units * pl_2[0].hp

            result_1 = pl_1_hp - dmg_2_to_1
            result_2 = pl_2_hp - dmg_1_to_2

            pl_1[0].units = ceil(result_1/pl_1[0].hp)
            pl_2[0].units = ceil(result_2/pl_2[0].hp)


class Warrior:
    role = 'Warrior'
    hp = 1
    dmg = {
        'Warrior': 1,
        'Archer': 2,
        'Mage': 0.5
    }
    def __init__(self, units):
        self.units = units
    def __str__(self):
        return str(self.role) + ': ' + str(self.units)

class Archer:
    role = 'Archer'
    hp = 1
    dmg = {
        'Warrior': 0.5,
        'Archer': 1, 
        'Mage': 2
    }
    def __init__(self, units):
        self.units = units        
    def __str__(self):
        return str(self.role) + ': ' + str(self.units)

class Mage:
    role = 'Mage'
    hp = 1
    dmg = {
        'Warrior': 2,
        'Archer': 0.5,
        'Mage': 1
    }
    def __init__(self, units):
        self.units = units
    def __str__(self):
        return str(self.role) + ': ' + str(self.units)


player1 = Army()
player2 = Army()

player1.player_choose()
player2.computer_choose()

player1.game(player2)
