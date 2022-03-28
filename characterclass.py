#!/usr/bin/env python3

from entity import Entity


class CharacterClass:
    game_states = ['Fighter', 'Mage', 'Thief']

    name = ''

    def __init__(self, name):
        Entity.__init__(self, name)

    def get_name(self):
        return self.name
