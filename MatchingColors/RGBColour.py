from XYZColour import XYZColour

class RGBColour:
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue


    def getComplimentaryColor(self):
        complimentaryRed = 255 - self.__red
        complimentaryGreen = 255 - self.__green
        complimentaryBlue = 255 - self.__blue
        return RGBColour(complimentaryRed, complimentaryGreen, complimentaryBlue)


    def getRGBValueForConversion(self, value):
        value = float(value) / 255
        if value > 0.04045:
            value = ((value + 0.055) / 1.055 ) ** 2.4
        else:
            value = value / 12.92
        return value * 100


    def convertRGBtoXYZ(self):
        redValue = self.getRGBValueForConversion(self.__red)
        greenValue = self.getRGBValueForConversion(self.__green)
        blueValue = self.getRGBValueForConversion(self.__blue)

        x = redValue * 0.4124 + greenValue * 0.3576 + blueValue * 0.1805
        y = redValue * 0.2126 + greenValue * 0.7152 + blueValue * 0.0722
        z = redValue * 0.0193 + greenValue * 0.1192 + blueValue * 0.9505

        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)

        xyzColour = XYZColour(0, 0, 0)
        xyzColour.setX(float(x) / 95.047)   # ref_X =  95.047   Observer= 2°, Illuminant= D65
        xyzColour.setY(float(y) / 100.0)    # ref_Y = 100.000
        xyzColour.setZ(float(z) / 108.883)   # ref_Z = 108.883

        return xyzColour


    def convertRGBtoLab(self):
        xyzColour = self.convertRGBtoXYZ()
        return xyzColour.convertXYZtoLab()


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


