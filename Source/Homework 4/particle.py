
class Particle:

    def __init__(self, sym, chg, massNumber):
        self.sym = sym
        self.chg = chg
        self.massNumber = massNumber

    def __str__(self):
        return self.sym

    def __repr__(self):
        className = self.__class__.__name__
        return "{}({!r}, {!r}, {!r})".format(
            className, self.sym, self.chg, self.massNumber)

    def __add__(self, other):
        return (self, other)

    def __eq__(self, other):

        if self.sym != other.sym:
            return False

        if self.chg != other.chg:
            return False

        if self.massNumber != other.massNumber:
            return False

        return True;

