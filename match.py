class Match:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def shoot(self, player, inBoard):
        curentPlayerScore = player.points - inBoard
        if (curentPlayerScore == 1 or curentPlayerScore < 0) and player.checkout == 2:
            print("No score")
            player.history[player.points] = 0
        elif curentPlayerScore < 0 and player.checkout == 1:
            print("No score")
        elif curentPlayerScore < 50 and player.checkout == 0:
            print("No score")
        else:
            player.points = curentPlayerScore
            player.history[curentPlayerScore] = 0

    def __str__(self):
        fillLen = 40
        heading = f'='*fillLen + f'\n{"|": <2}{self.p1.name.center(16)}{"|": >2}{"|": <2}{self.p2.name.center(16)}{"|": >2}\n' + "="*fillLen + "\n"
        scoring = ""
        print(self.p1.history)
        print(self.p2.history)
        for (k,v), (k2,v2) in zip(self.p1.history.items(), self.p2.history.items()):
            scoring += f'|' + f'{str(k)} | {str(v)}'.center(18) + f'|'
            scoring += f'|' + f'{str(k2)} | {str(v2)}'.center(18) + f'|\n'

        if len(self.p1.history) > len(self.p2.history):
                scoring += f'|' + f'{str(list(self.p1.history)[-1])} | {str(self.p1.history[list(self.p1.history)[-1]])}'.center(18) + f'|'
                scoring += f'|' + f'next | next'.center(18) + f'|\n'
        return heading + scoring
