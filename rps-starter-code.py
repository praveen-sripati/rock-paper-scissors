#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        self.player_move = input("Rock, paper, scissors? > ")
        if (self.player_move.lower() == "rock"
            or self.player_move.lower() == "paper"
            or self.player_move.lower() == "scissors"
            or self.player_move.lower() == "quit"):
            return self.player_move.lower()
        else:
            return self.move()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_scores = [0, 0]

    # This function provides information of each round w.r.t winning of player
    def round_info(self, move1, move2, score, win_values):
        self.player_scores[score] += 1
        print(f"{move1} beats {move2}")
        print(f"** PLAYER {win_values[score]} WINS **")
        print(f"Score: Player One {self.player_scores[0]}, Player Two {self.player_scores[1]}")
        print("( Type \"quit\" to exit from game.)\n")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        # returns "quit" if input of HumanPlayer is "quit"
        if move1 == "quit":
            return move1

        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.round_info(move1, move2, 0, ["ONE", "TWO"])
        elif beats(move2, move1):
            self.round_info(move1, move2, 1, ["SOME", "TWO"])
        else:
            print("** TIE **")
            print(f"Score: Player One {self.player_scores[0]}, Player Two {self.player_scores[1]}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        round = 0
        print("\nGame start!")
        print("-"*16)
        while True:
            round += 1
            print(f"Round {round}:")
            quit_game = self.play_round()

            #check whether the player wants to quit or not
            if quit_game == "quit":
                break
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
