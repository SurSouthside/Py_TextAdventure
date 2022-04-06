#!/usr/bin/env python3

from entity import Entity
from characterclass import CharacterClass


class Character(Entity):

    def __init__(self, name):
        Entity.__init__(self, name)
        self._char_class = CharacterClass('')
        self._level = 0
        self._xp = 0
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

    def set_name(self, name):
        self._name = name



