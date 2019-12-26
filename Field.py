class Field():
    def __init__(self, x, y, z):
        self.field = [[[0] * x] * y] * z

class Piece():
    def __init__(self, pieceType, color):
        self.piece = {
                1: 'Line',
                2: 'Cube',
                3: 'SLeft',
                4: 'SRight',
                5: 'Bomb',
                }[pieceType]
        self.color = {
                1: 'Red',
                2: 'Blue',
                3: 'Yellow',
                4: 'Green',
                5: 'Orange',
                6: 'Purple',
                7: 'Pink',
                8: 'Brown',
                9: 'White',
                10: 'Black',
                }[color]

