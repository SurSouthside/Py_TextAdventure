#!/usr/bin/env python3

from character import Character


class Player(Character):

    def __init__(self, name):
        Character.__init__(self, name)

    def get_name(self):
        return self._name
