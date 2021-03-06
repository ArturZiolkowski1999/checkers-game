import pygame


class Drawings:
    def __init__(self, window):
        self.window = window
        self.recSize = 100
        pass

    def drawBoard(self, board):
        matrix = board.getMatrix()
        for row in matrix:
            for rectangle in row:
                x, y = rectangle
                coordinateX = x - 50
                coordinateY = y - 50

                pygame.draw.rect(self.window, (0, 0, 0), ((coordinateX, coordinateY), (self.recSize, self.recSize)))

    def drawPawns(self, pawnList):
        for pawn in pawnList.getList():
            pawn.draw()
