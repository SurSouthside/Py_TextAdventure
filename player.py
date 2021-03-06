#!/usr/bin/env python3

from character import Character
import random


class Player(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        self._char_class = ''

    def get_char_class(self):
        return self.char_class

    def set_char_class(self, char_class):
        self._char_class = char_class

    def generate_starting_stats(self, char_class):
        self._level = 1
        self._xp = 0
        match char_class:
            case 'Fighter':
                print("You selected Fighter")
                self._hp = random.randint(70, 75)
                self._mp = random.randint(5, 10)
                self._strength = random.randint(15, 20)
                self._defense = random.randint(15, 20)
                self._magic = random.randint(5, 10)
                self._spirit = random.randint(10, 15)
                self._agility = random.randint(25, 30)
                self._luck = random.randint(5, 10)
            case 'Mage':
                print("You selected Mage")
                self._hp = random.randint(40, 45)
                self._mp = random.randint(20, 25)
                self._strength = random.randint(5, 10)
                self._defense = random.randint(5, 10)
                self._magic = random.randint(15, 20)
                self._spirit = random.randint(20, 25)
                self._agility = random.randint(10, 15)
                self._luck = random.randint(5, 10)
            case 'Thief':
                print("You selected Thief")
                self._hp = random.randint(55, 60)
                self._mp = random.randint(10, 15)
                self._strength = random.randint(10, 15)
                self._defense = random.randint(10, 15)
                self._magic = random.randint(5, 10)
                self._spirit = random.randint(15, 20)
                self._agility = random.randint(40, 45)
                self._luck = random.randint(15, 20)

    def create_character(self, name, char_class):
        print(char_class + " character created")
        self.set_name(name)
        self.set_char_class(char_class)
        self.generate_starting_stats(char_class)
        return self
