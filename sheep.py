class Sheep():
    """
    A class used to represent a Sheep. Every sheep has following attributes:
    x: x-coordinate
    y: y-coordinate
    velocity: velocity of the sheep
    vector: vector of the sheep
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return f"Sheep X: {self.x}, Y: {self.y}"


