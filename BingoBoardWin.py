from BingoBoardClass import BingoBoard

class BingoBoardWin:
    def __init__(self, BingoBoard: BingoBoard):
        self.board = BingoBoard
    # helper funcitons
    def _isSquare(self) -> bool:
        return self.board.height == self.board.width

    def _leftDiagnalCheck(self) -> list[int]:
        if not(self._isSquare()):
            return None
        height = self.board.height
        width = self.board.width
        i = 0
        win = []
        while i < height and i < width:
            if self.board.bingoCard[i][i] > 0:
                return None
            win.append(abs(self.board.bingoCard[i][i]))
            i += 1
        return win
    
    def _rightDiagnalCheck(self) -> list[int]:
        if not(self._isSquare()):
            return None
        width = self.board.width
        i = width - 1
        win = []
        while i >= 0:
            if self.board.bingoCard[i][i] > 0:
                return None
            win.append(abs(self.board.bingoCard[i][i]))
            i -= 1
        return win

    def _diagnalCheck(self) -> bool:
        ret = self._leftDiagnalCheck()
        if(ret):
            return ret
        ret = self._rightDiagnalCheck()
        if(ret):
            return ret
        return None
    
    def _verticalCheck(self, col: int) -> bool:
        win = []
        for row in range(self.board.height):
            if(self.board.bingoCard[row][col] > 0):
                return None
            win.append(abs(self.board.bingoCard[row][col]))
        return win

    def _horizontalCheck(self, row: int) -> bool:
        win = []
        for col in range(self.board.width):
            if(self.board.bingoCard[row][col] > 0):
                return None
            win.append(abs(self.board.bingoCard[row][col]))
        return win

    def _markedNormalWin(self, row: int, col: int) -> bool:
        win = []
        if(row == col):
            ret = self._diagnalCheck()
            if(ret):
                win.append(ret)
        ret = self._verticalCheck(col)
        if(ret):
            win.append(ret)
        ret = self._horizontalCheck(row)
        if(ret):
            win.append(ret)
        if len(win) == 0:
            return None
        else:
            return win
        
    def _unMakredNormalWin(self) -> bool:
        """the board has to not be empty, don't check for an empty board"""
        win = []
        for row in range(self.board.height):
            ret = self._horizontalCheck(row)
            if(ret):
                win.append(ret)
        for col in range(self.board.width):
            ret = self._verticalCheck(col)
            if(ret):
                win.append(ret)
        ret = self._diagnalCheck()
        if(ret):
            win.append(ret)
        if len(win) == 0:
            return None
        else:
            return win
    #end of helper funcitons
    
    def normalWin(self, row: int = None, col: int = None) -> bool:
        """You have two options, you can either put down where you just marked for a faster check.
           Or we checking the whole board.
        """
        if(row == None or col == None):
            return self._unMakredNormalWin()
        else:
            return self._markedNormalWin(row, col)
                    