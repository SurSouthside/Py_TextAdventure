#!/usr/bin/env python3

class Game:

    game_states = ['started', 'new', 'continued']

    def __init__(self, state):
        self.state = 'started'

    def startGame(self):
        print("Welcome to Text Adventure")
        print("Select An Option:")
        print("1. New Game")
        print("2. Continue")
        start_screen_choice = input()
        if start_screen_choice == '1':
            print("New Game selected")
        elif start_screen_choice == '2':
            print("Continue selected")
        else:
            print("Option not recognized")
