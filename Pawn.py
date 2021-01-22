import time


class Pawn:

    def __init__(self, coordinateX, coordinateY, radius, color, canvas, window):
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY
        self.color = color
        self.radius = radius
        self.canvas = canvas
        self.window = window
        self.drawing = self.draw()
        self.alive = True
        self.radius = radius

    def draw(self):

        x0 = self.getCordinateX() - self.getRadius()
        y0 = self.getCordinateY() - self.getRadius()
        x1 = self.getCordinateX() + self.getRadius()
        y1 = self.getCordinateY() + self.getRadius()

        outline = "#5c000b"

        if self.getColor() == "blue":
            outline = "#0b51a3"

        return self.getCanvas().create_oval(x0, y0, x1, y1, fill=self.getColor(), width=2, outline=outline)

    def movePawn(self, newPosX, newPosY):

        print("move")
        pawn = self.drawing
        moving = True
        startingX = self.getCordinateX()
        startingY = self.getCordinateY()
        speedX = 4
        speedY = 4
        positionCorrection = self.getRadius() * -1

        self.setCordinateX(newPosX)
        self.setCordinateY(newPosY)

        if self.getColor() == "red":
            if startingX > newPosX:
                speedX *= -1

        elif self.getColor() == "blue":
            speedY *= -1
            if startingX > newPosX:
                speedX *= -1

        while moving:
            pawn_pos = self.getCanvas().coords(pawn)
            self.getCanvas().move(pawn, speedX, speedY)
            self.getWindow().update()
            time.sleep(0.01)
            x, y, r, r = pawn_pos
            print(x, y)
            if x == newPosX + positionCorrection and y == newPosY + positionCorrection:
                moving = False

    def isMovePossible(self, pawnList, listOfThisPawn, moveCordsX, moveCordSy):

        for pawn in pawnList.getList():
            if (pawn.getCordinateX() == moveCordsX) and (pawn.getCordinateY() == moveCordSy):
                print("False")
                return False

        for pawn in listOfThisPawn.getList():
            if (pawn.getCordinateX() == moveCordsX) and (pawn.getCordinateY() == moveCordSy) and pawn != self:
                print("False")
                return False

        if (self.getCordinateX() == moveCordsX) and (self.getCordinateY() == moveCordSy):
            print("You are here fool!")
            return False
        print("True")
        return True

    def pawnDestroy(self):
        self.alive = False

    def getCordinateX(self):
        return self.coordinateX

    def setCordinateX(self, newCoordinateX):
        self.coordinateX = newCoordinateX

    def getCordinateY(self):
        return self.coordinateY

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def getRadius(self):
        return self.radius

    def getCanvas(self):
        return self.canvas

    def getWindow(self):
        return self.window

    def setCordinateY(self, newCoordinateY):
        self.coordinateY = newCoordinateY
