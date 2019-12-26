#!/usr/bin/python3

#from graphics import *
from random import *

from Field import *

X = Z = 10; Y = 50
f = Field(X, Y, Z)

def curCoord(piece, dirHor, dirVer, x, y, z):
    if piece == 'Line':
        if dirVer == 0:
            if dirHor == 0:
                return list((x - 1, y, z), (x, y, z), (x + 1, y, z), (x + 2, y, z))
            elif dirHor == 1:
                return list((x, y, z - 1), (x, y, z), (x, y, z + 1), (x, y, z + 2))
            elif dirHor == 2:
                return list((x + 1, y, z), (x, y, z), (x - 1, y, z), (x - 2, y, z))
            else:
                return list((x, y, z + 1), (x, y, z), (x, y, z - 1), (x, y, z - 2))
        else:
            return list((x, y - 1, z), (x, y, z), (x, y + 1, z), (x, y + 2, z))

def updateField(curCoord):
    for coord in curCoord:

def checkCollision(curCoord, color):
    for coord in curCoord:
        if (coord[0] > X - 1 or coord[0] < 0) or \
            (coord[1] > Y - 1 or coord[1] < 0) or \
            (coord[2] > Z - 1 or coord[2] < 0):
                return 'border'
        elif (f.field[coord[0]][coord[1] - 1][coord[2]] != 0):
            updateField(curCoord)
            return 'pieceSet'
    return False


def main():
    pieceX = pieceY = pieceZ = 0
    dirHor = dirVer = 0
    p = None; color = None
    prevCoord = [], curCoord = []
    pieceActive = gameOver = False

    while not gameOver:
        if not pieceActive:
            p = Piece(random(1, 5), random(1, 10))
            pieceY = 0
            pieceX = random(0, X - 1)
            pieceZ = random(0, Z - 1)
            color = p.color
        prevCoord = currCoord
        currCoord = getCoord(p.piece, dirHor, dirVer, pieceX, pieceY, pieceZ)
        if not collision(curCoordList, color):
            pass
            # currCoord =

        #newList = nxtCoord(dirHor, dirVer, pieceX, pieceY, pieceZ)
        #check collision

if __name__ == "__main__":
    main()
