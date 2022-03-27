#!/usr/bin/env python3

from player import Player

class Game:

    game_states = ['started', 'new', 'continued']

    def __init__(self, state):
        self.state = state

    def process_new_game(self):
        the_player = Player('Default')
        char_name = input("Enter your characters name:")
        print("Character name: " + char_name)

    def start_game(self):
        print("Welcome to Text Adventure")
        print("Select An Option:")
        print("1. New Game")
        print("2. Continue")
        start_screen_choice = input()
        if start_screen_choice == '1':
            print("New Game selected")
            the_player = self.process_new_game()
        elif start_screen_choice == '2':
            print("Continue selected")
        else:
            print("Option not recognized")


