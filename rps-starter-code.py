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
            or self.player_move.lower() == "scissors"):
            return self.player_move
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

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.player_scores[0] += 1
            print(f"{move1} beats {move2}")
            print("** PLAYER ONE WINS **")
            print(f"Score: Player One {self.player_scores[0]}, Player Two {self.player_scores[1]}")
        elif beats(move2, move1):
            self.player_scores[1] += 1
            print(f"{move2} beats {move1}")
            print("** PLAYER TWO WINS **")
            print(f"Score: Player One {self.player_scores[0]}, Player Two {self.player_scores[1]}")
        else:
            print("** TIE **")
            print(f"Score: Player One {self.player_scores[0]}, Player Two {self.player_scores[1]}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        round = 0
        print("Game start!")
        print(f"Round {round}:")
        self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
