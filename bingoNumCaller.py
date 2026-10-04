from random import randint
from AVLTree import BST

class numCaller:
    def __init__(self, maxNum: int = 75):
        self.maxNum = maxNum
        self.nums = [i + 1 for i in range(maxNum)]
        self.BST = BST()

    def callNum(self) -> int:
        if len(self.nums) == 0:
            return None
        num = self.nums.pop(randint(0, len(self.nums) - 1))
        self.put(num)
        return num

    def put(self, num: int) -> None:
        self.BST.addNum(num)
    
    def clear(self) -> None:
        self.BST.clearBST()
        self.nums = [i + 1 for i in range(self.maxNum)]

    def wasNumCalled(self, num: int) -> bool:
        return self.BST.numInTree(num)
    
    def getAllNums(self) -> list[int]:
        return self.BST.bstToList()