#!/usr/bin/env python3

from entity import Entity


class CharacterClass(Entity):
    possible_classes = ['Fighter', 'Mage', 'Thief']

    def __init__(self, name):
        Entity.__init__(self, name)

    def get_name(self):
        return self._name
