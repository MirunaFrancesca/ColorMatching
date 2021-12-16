from LabColour import LabColour

class XYZColour:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def getXYZValueForConversion(self, value):
        if value > 0.008856:
            value = value ** 0.3333333333333333
        else:
            value = (7.787 * value) + (16 / 116)
        return value


    def convertXYZtoLab (self):
        xValue = self.getXYZValueForConversion(self.__x)
        yValue = self.getXYZValueForConversion(self.__y)
        zValue = self.getXYZValueForConversion(self.__z)

        L = ( 116 * yValue) - 16
        a = 500 * (xValue - yValue)
        b = 200 * (yValue - zValue)

        labColour = LabColour(0, 0, 0)
        labColour.setL(round(L, 4))
        labColour.setA(round(a, 4))
        labColour.setB(round(b, 4))

        return labColour


    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setZ(self, z):
        self.__z = z

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z