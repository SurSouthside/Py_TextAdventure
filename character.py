#!/usr/bin/env python3

from entity import Entity
import random


class Character(Entity):

    def __init__(self, name):
        Entity.__init__(self, name)
        self._hp = 0
        self._mp = 0
        self._strength = 0
        self._defense = 0
        self._magic = 0
        self._spirit = 0
        self._agility = 0
        self._luck = 0

    def get_name(self):
        return self._name

    def generate_starting_stats(self, char_class):
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
                self._agility = random.randint(5, 10)
            case 'Mage':
                print("You selected Mage")
            case 'Thief':
                print("You selected Thief")


    def create_character(self, name, char_class):
        print(char_class + "character created")
        self.generate_starting_stats(self, char_class)
        return self
