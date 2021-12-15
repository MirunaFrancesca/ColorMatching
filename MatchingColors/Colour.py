class Colour:
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def getComplimentaryColor(self):
        complimentaryRed = 255 - self.__red
        complimentaryGreen = 255 - self.__green
        complimentaryBlue = 255 - self.__blue
        return Colour(complimentaryRed, complimentaryGreen, complimentaryBlue)

    def setRed(self, red):
        self.__red = red

    def setGreen(self, green):
        self.__green = green

    def setBlue(self, blue):
        self.__blue = blue

    def getRed(self, red):
        return self.__red

    def getGreen(self, green):
        return self.__green

    def getBlue(self, blue):
        return self.__blue


