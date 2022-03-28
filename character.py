#!/usr/bin/env python3

from entity import Entity


class Character(Entity):

    def __init__(self, name):
        Entity.__init__(self, name)

    def get_name(self):
        return self._name
