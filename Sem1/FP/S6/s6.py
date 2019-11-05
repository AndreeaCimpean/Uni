from game import *
'''
Bulls and cows
This is a game played by the human player and the computer as it follows:
1. The computer selects a random 4-digits number, which has no repeating digits (e.g. 1234, 9508, 6789 are all okay)
2. The player tries to guess the number
3. Each turn, the player enters a 4-digit guess
4. The computer tells how many bulls (correct digit in the correct place) and cows (correct digit, but incorrect place)
   there are in the latest guess
5. Game is over when the number is guessed. The aim is to do this over the smallest number of turns possible

UPDATE:
    - computer picks a word withou repeeted letters (isogram) (from memory, or better from an input file)
    - At new game, computer tells th user the word's length
    - Trying the same word twice loses the game :(
    - The result of the rules still apply
'''

'''
3760

1234 ->0B1C
2769 ->
'''

class UI:
    def __init__(self, game):
        self._game = game

    def print_menu(self):
        print("BULLS AND COWS")
        print("   1 to start a new game")
        print("   x to exit")

    def start(self):
        '''
        1.  Print the menu:
            - Start new game:
                - Read user guess
                - self._game determines if repeated guess - lose
                - self._game determines #bulls and #cows returned to the UI
            - Exit
        2. Once the game is over, print 
        '''
        while True:
            self.print_menu()
            command = input("> ")
            if command == "1":
                self._game.newGame()
                userGuess = int(input("Your guess > "))
                while not self._game.isVictory(userGuess):
                    try:
                        d = self._game.guess(userGuess)
                        cows = d['cows']
                        bulls = d['bulls']
                        print(str(cows) + ' cows')
                        print(str(bulls) + ' bulls')
                        userGuess = int(input("Your guess > "))
                        
                    except GameException as ge:
                        print(ge)
                        return
                print('Yay')

            elif command =="x":
                return
            else:
                print("Invalid command")
    
g = Game()    
ui = UI(g)
ui.start()