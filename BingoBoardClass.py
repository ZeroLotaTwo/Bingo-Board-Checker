from random import randint

class BingoBoard:
    # def dont change the heigjt and width
    # infinite loop will happem if height >= 15
    def __init__(self, height: int = 5, width: int = 5, MaxNum: int = 75):
        self.height = height
        self.width = width
        self.maxNum = MaxNum
        self.nextLetter = MaxNum // 5 #Note I'm not sure how this works if the board increases in size so I decided to use five because 75/5 = 15 for default board
        lo = 1
        hi = self.nextLetter
        self.freeSpaceRow = height // 2
        self.freeSpaceCol = width // 2
        self.bingoCard = [[] for i in range(height)]
        # initialization of self.bingoCard
        usedNumsStack = []
        numRange = len(range(lo,hi))
        #this code here will fill the board vertically instead of rastor way.
        for _ in range(height):
            for row in range(width):
                num = randint(lo, hi)
                while num in usedNumsStack and len(usedNumsStack) != numRange:
                    num = randint(lo,hi)
                if len(usedNumsStack) == numRange:
                    raise "Can't fill in the board with the given range"
                self.bingoCard[row].append(num)
                usedNumsStack.append(num)
            lo += self.nextLetter
            hi += self.nextLetter
            usedNumsStack.clear()
        self.bingoCard[self.freeSpaceRow][self.freeSpaceCol] = 0
    
    
    def getBingoCard(self) -> list[list[int]]:
        return self.bingoCard
    
    def markBoard(self, row: int, col: int) -> None:
        self.bingoCard[row][col] = -self.bingoCard[row][col]
    
    def markNum(self, num: int) -> tuple[int, int]:
        if(num == None):
            return
        if(0 >= num or num > self.maxNum):
            return
        col = (num - 1) // self.nextLetter
        if(col == self.width):
            col -= 1
        for row in range(len(self.bingoCard)):
            if(abs(self.bingoCard[row][col]) == num):
                self.markBoard(row, col)
                return (row, col)
        return None

    def clearBoard(self):
        for row in self.bingoCard:
            for col in range(len(row)):
                row[col] = abs(row[col])