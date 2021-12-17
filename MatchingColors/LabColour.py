from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976


class LabColour:
    def __init__(self, L, a, b):
        self.__L = L
        self.__a = a
        self.__b = b

    def __str__(self):
        return "L = " + str(self.getL()) + "\na = " + str(self.getA()) + "\nb = " + str(self.getB())

    def computeDeltaE(self, otherColour):
        # delta-e is computed using the Cie76 algorithm
        # delta-e < 2 => equivalent colours
        color1 = LabColor(lab_l=self.getL(), lab_a=self.getA(), lab_b=self.getB())
        color2 = LabColor(lab_l=otherColour.getL(), lab_a=otherColour.getA(), lab_b=otherColour.getB())
        delta_e = delta_e_cie1976(color1, color2)
        return delta_e

    def setL(self, L):
        self.__L = L

    def setA(self, a):
        self.__a = a

    def setB(self, B):
        self.__b = B

    def getL(self):
        return self.__L

    def getB(self):
        return self.__b

    def getA(self):
        return self.__a
