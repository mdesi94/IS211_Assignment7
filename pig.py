import random


class Die:
    def __init__(self):
        self.sides = 6
        self.roll()

    def roll(self):
        self.value = int(random.random() * self.sides + 1)


class Game:
    def __init__(self, p1, p2):
        self.die = Die()
        self.p1 = p1
        self.p2 = p2
    """
    main gameplay, checks for a winner or continues gameplay
    """
    def play(self):
        while self.p1.score <= 20 and self.p2.score <= 20:
            self.p1.turn()
            if self.p1.score < 20:
                self.p2.turn()
        if self.p1.score > self.p2.score:
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')


class Player:
    def __init__(self, title):
        self.name = title
        self.score = 0
        self.die = Die()

    """
    while loop continues player's turn until 1 is rolled or 'h' entered.
    """

    def turn(self):
        round_score = 0
        roll_again = 'r'

        while roll_again == 'r':
            self.die.roll()
            roll = self.die.value
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                roll_again = 'n'
            else:
                print('{} rolled a {}'.format(self.name, roll))
                round_score = round_score + roll
                print("{}'s round score is {}".format(self.name, round_score))
                roll_again = input('Roll = r or Hold = h?  ')
        self.score += round_score
        print("{}'s turn is over".format(self.name))
        print("{}'s total score is {}\n\n".format(self.name, self.score))


if __name__ == "__main__":

    print('Lets play Pig!')
    p1 = Player('Player 1')
    p2 = Player('Player 2')
    pig = Game(p1, p2)
    pig.play()
    print()
    print('Rerun program to play again')