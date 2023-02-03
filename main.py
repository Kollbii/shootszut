from art import text2art
from player import Player
from match import Match
import json
import os

if __name__ == "__main__":
    print("Welcome to ShootSzut")
    print("CLI scoring system for Darts")
    print(text2art("ShootSzut"))
    print("\\\\\\\\\\\\       ________\n >>>>>>---==(________)------\n//////")

    # Declare players
    p1 = Player("kollibosonerek")
    p2 = Player("Shoot")

    # Declare game settings
    m = Match(p1, p2)

    # Welcome banner for game start
    # print(p1)
    # print(p2)

    with open("checkout.json") as checkouts:
        data = json.load(checkouts)

    # print(data)

    turn = 1
    while True:
        try:
            playerToShoot = Player("Dummy")
            if turn == 1:
                # print(f"{p1.name} turn")
                playerToShoot = p1
                # print(playerToShoot)
                turn = 2
            else:
                # print(f"{p2.name} turn")
                playerToShoot = p2
                # print(playerToShoot)
                turn = 1
            os.system('cls||clear')
            print(text2art("ShootSzut"))
            print("\\\\\\\\\\\\       ________\n >>>>>>---==(________)------\n//////")
            print(m)
            inBoard = int(input(">> "))
            playerToShoot.history[playerToShoot.points] = inBoard
            m.shoot(playerToShoot, inBoard)
        except KeyboardInterrupt:
            exit()
