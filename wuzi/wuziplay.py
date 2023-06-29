
class WuziPlay:
    def __init__(self, chessBoardSize = 16) -> None:
        self.chessBoardSize=chessBoardSize
        self.isPlaying = False

        pass

    def start(self):
        self.chess = [[-1 for i in range(self.chessBoardSize+1)] for i in range(self.chessBoardSize+1)]
        self.currentPlayer = 0
        self.isPlaying = True
        pass

    # 返回-1 表示当前位置不可下棋
    # 返回99表示当前位置可下棋，但未决出胜负
    # 返回0表示当前位置可下棋，player 0胜利
    # 返回1表示当前位置可下棋，player 1胜利
    def putChess(self, x, y):
        if not self.isPlaying:
            return -1

        # 确定下棋坐标
        if self.chess[x][y] != -1:
            return -1
        
        self.chess[x][y] = self.currentPlayer
        self.currentPlayer = (self.currentPlayer+1) % 2

        if self.gameOverCheck(x, y):
            self.isPlaying = False
            return self.currentPlayer
        else:
            return 99
    

    # 返回True表示游戏结束
    def gameOverCheck(self, x, y):
        count = 0
        for i in range(x + 1, self.chessBoardSize+1):  # 向右搜索
            if self.chess[i][y] == self.chess[x][y]:
                count += 1
            else:
                break
        for i in range(x, 0, -1):  # 向左搜索
            if self.chess[i][y] == self.chess[x][y]:
                count += 1
            else:
                break
        if count == 5:
            return True
        count = 0

        for i in range(y + 1, self.chessBoardSize+1):  # 向下搜索
            if self.chess[x][i] == self.chess[x][y]:
                count += 1
            else:
                break
        for i in range(y, 0, -1):  # 向上搜索
            if self.chess[x][i] == self.chess[x][y]:
                count += 1
            else:
                break
        if count == 5:
            return True
        count = 0

        for i, j in zip(range(x+1, self.chessBoardSize+1), range(y+1, self.chessBoardSize+1)):  # 向右下搜索
            if self.chess[i][j] == self.chess[x][y]:
                count += 1
            else:
                break
        for i, j in zip(range(x, 0, -1), range(y, 0, -1)):  # 向左上搜索
            if self.chess[i][j] == self.chess[x][y]:
                count += 1
            else:
                break
        if count == 5:
            return True
        count = 0

        for i, j in zip(range(x - 1, 0, -1), range(y + 1, self.chessBoardSize+1)):  # 向左下搜索
            if self.chess[i][j] == self.chess[x][y]:
                count += 1
            else:
                break
        for i, j in zip(range(x, self.chessBoardSize+1), range(y, 0, -1)):  # 向右上搜索
            if self.chess[i][j] == self.chess[x][y]:
                count += 1
            else:
                break
        if count == 5:
            return True
        count = 0

    def currentPlayer(self):
        return self.currentPlayer
    
    def isPlaying(self):
        return self.isPlaying
