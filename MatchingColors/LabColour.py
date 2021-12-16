class LabColour:
    def __init__(self, L, a, b):
        self.__L = L
        self.__a = a
        self.__b = b

    def __str__(self):
        return "L = " + str(self.getL()) + "\na = " + str(self.getA()) + "\nb = " + str(self.getB())

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
