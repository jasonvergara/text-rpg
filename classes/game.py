import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_actions(self):
        i = 1
        print('\n\t' + bcolors.BOLD + self.name + bcolors.ENDC)
        print('\t' + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print(f"\t\t{i}: {item}")
            i += 1

    def choose_magic(self):
        i = 1
        print('\n\t' + bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print(f"\t\t{i}: {spell.name} (cost: {spell.cost})")
            i += 1

    def choose_item(self):
        i = 1
        print('\n\t' + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print(f"\t\t{i}. {item['item'].name}: {item['item'].description} (x{item['quantity']})")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print('\n\t' + bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(f"\t\t{i}. {enemy.name}")
                i += 1
        choice = int(input("\tChoose target: ")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ''
        hp_ticks = (self.hp / self.maxhp) * 48

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 48:
            hp_bar += ' '

        print(" " * 26 + "_" * 48)
        print(bcolors.BOLD + f"{self.name:<10}:{self.hp:>7}/{self.maxhp:<6}|" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ''
        hp_ticks = (self.hp / self.maxhp) * 20

        mp_bar = ''
        mp_ticks = (self.mp / self.maxmp) * 10

        while hp_ticks > 0:
            hp_bar += "█"
            hp_ticks -= 1

        while len(hp_bar) < 20:
            hp_bar += ' '

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '

        print(" " * 26 + "_" * 20 + " " * 18 + "_" * 10)
        print(bcolors.BOLD + f"{self.name:<10}:{self.hp:>7}/{self.maxhp:<6}|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + f"|{self.mp:>9}/{self.maxmp:<5} |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        if self.mp < spell.cost:
            return spell, 0
        else:
            return spell, magic_dmg
