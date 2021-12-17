from RGBColour import RGBColour


class Controller:
    def __init__(self, inFilename):
        self.__inFilename = inFilename
        self.__colours = []
        self.__matches = {}
        self.__palette = {
            "red": RGBColour(255, 0, 0),
            "orange": RGBColour(255, 127, 0),
            "yellow": RGBColour(255, 255, 0),
            "green": RGBColour(0, 255, 0),
            "blue": RGBColour(0, 0, 255),
            "indigo": RGBColour(75, 0, 130),
            "violet": RGBColour(148, 0, 211),
            "pink": RGBColour(255, 192, 203),
            "brown": RGBColour(150, 75, 0),
            "gray": RGBColour(128, 128, 128),
            "black": RGBColour(255, 255, 255),
            "white": RGBColour(0, 0, 0)
        }


    def readFromFile(self):
        faFile = open(self.__inFilename, "r")
        lines = faFile.readlines()

        for line in lines:
            if line != "\n":
                r, g, b = line.split()
                self.__colours.append(RGBColour(int(r), int(g), int(b)))

        faFile.close()


    def getSimilarBasicColour(self, rgbColour):
        minColourDistance = 100
        similarBasicColour = []
        labColour = rgbColour.convertRGBtoLab()
        for colour in self.__palette.keys():
            labPaletteColour = self.__palette[colour].convertRGBtoLab()
            currentColourDistance = labColour.computeDeltaE(labPaletteColour)
            if currentColourDistance < minColourDistance:
                similarBasicColour = [colour]
                minColourDistance = currentColourDistance
            if currentColourDistance == minColourDistance:
                similarBasicColour.append(colour)

        return similarBasicColour

    def findClosestComplimentaryColours(self, colour):
        complimentaryColour = colour.getComplimentaryColor()
        similarComplimentaryBasicColour = self.getSimilarBasicColour(complimentaryColour)
        allComplimentaryColours = []
        for colour in self.__colours:
            if self.getSimilarBasicColour(colour) == similarComplimentaryBasicColour:
                allComplimentaryColours.append(colour)

        return allComplimentaryColours


    def matchColours(self):
        for colour in self.__colours:
            self.__matches[colour] = self.findClosestComplimentaryColours(colour)


    def writeToFile(self, outFilename):
        outFile = open(outFilename, "w")
        toPrint = ""
        for colour in self.__matches.keys():
            toPrint += "Colour " + str(colour) + " has the following matches:\n"
            for matchingColour in self.__matches[colour]:
                toPrint += str(matchingColour) + " "
            toPrint += "\n"

        outFile.write(toPrint)
        outFile.close()





