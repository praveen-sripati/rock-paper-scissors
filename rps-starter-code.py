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

class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return self.my_move

class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.players_score = [0, 0]

    # This function provides information of each round w.r.t winning of player
    def round_info(self, move1, move2, score, win_values):
        self.players_score[score] += 1
        print(f"{move1.upper()} beats {move2.upper()}")
        print(f"** PLAYER {win_values[score]} WINS **")
        print(f"Score: Player One {self.players_score[0]}, Player Two {self.players_score[1]}\n")

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
            self.round_info(move2, move1, 1, ["SOME", "TWO"])
        else:
            print("** TIE **")
            print(f"Score: Player One {self.players_score[0]}, Player Two {self.players_score[1]}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def rounds_input(self):
        user_input = input("Enter number of rounds: ")
        try:
            if int(user_input) > 0:
                return int(user_input)
            else:
                print("Enter a positive number!")
                self.rounds_input()
        except ValueError:
            print("Enter a number not a string!")
            self.rounds_input()

    def play_game(self):
        round = 0
        print("\nGame start!")
        print("="*13 + "\n")
        rounds = self.rounds_input()
        for round in range(rounds):
            round += 1
            print("-"*45)
            print(f"Round {round}: ( Type \"quit\" to exit from game )")
            print("-"*45)
            quit_game = self.play_round()

            # Check whether the player wants to quit or not
            if quit_game == "quit":
                break
        print("-"*45)
        print(f"Final Score: Player One {self.players_score[0]}, Player Two {self.players_score[1]}\n")
        if self.players_score[0] > self.players_score[1]:
            print(f"Final Winner is PLAYER ONE!! Congratulations!")
        elif self.players_score[1] > self.players_score[0]:
            print(f"Final Winner is PLAYER TWO!! Congratulations!")
        else:
            print("It's A TIE!!")

        print("Game over!")
        print("-"*45)


if __name__ == '__main__':
    game = Game(RandomPlayer(), CyclePlayer())
    game.play_game()
