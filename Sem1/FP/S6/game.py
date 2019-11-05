import random

class GameException(Exception):
    '''
    GameException is a Python Exception
    '''
    def __init__(self,message):
        super().__init__(message)

class Game:
    def _generateNumber(self):
        '''
        Generate a valid number
        '''
        a = random.randint(1,9)
        b = random.randint(0,9)
        while b == a:
            b = random.randint(0,9)
        c = random.randint(0,9)
        while c == a or c == b:
            c = random.randint(0,9)
        d = random.randint(0,9)
        while d == a or d == b or d == c:
            d = random.randint(0,9)
        number = a*1000 + b*100 + c*10 + d
        return number

    def newGame(self):
        self._history = []
        self._number = self._generateNumber()

    def isRepeatedGuess(self,userGuess):
        '''
            If yes -> game lost
        '''
        pass

    def isVictory(self,userGuess):
        return int(userGuess) == self._number
    
    def guess(self,userGuess):

        if userGuess in self._history:
            raise GameException("Repeated Guess")
        self._history.append(int(userGuess))
        lstUser = [int(userGuess)%10, int(userGuess)%100/10, int(userGuess)%1000/10, int(userGuess)%1000]
        lstComputer = [self._number%10, self._number%100/10, self._number%1000/10, self._number%1000]
        cows = 0
        bulls = 0

        for i in range(0,4):
            if lstUser[i] == lstComputer[i]:
                bulls += 1
        
        for i in range(0,4):
            if lstUser[i] in lstComputer:
                cows += 1
        
        return {"bulls":bulls,"cows":cows}


g = Game()
g.newGame()
g.guess(1111)
try:
    cows = g.guess(1111)['cows']
except GameException:
    print("nay")



'''

1. Generate 1000 numebers?
2. For each generated number:
    number in [1023,9876]
    check no duplicate digits
'''
def test_generate_number():
    for i in range(0,1000):
        g = Game()
        no = g._generateNumber()
        assert no >=1023 and no <= 9876
        a = no%10
        b = no%100/10
        c = no%1000/10
        d = no%1000
        assert a != b and a != c and a != d and b != c and b != d and c != d 