from random import random, randint
from RGBColour import RGBColour


class Controller:
    def __init__(self, inFilename):
        self.__inFilename = inFilename
        self.__colours = []
        self.__matches = {}
        self.__similarMainColors = {}
        self.__palette = {
            "red": RGBColour(255, 0, 0),
            "orange": RGBColour(255, 127, 0),
            "yellow": RGBColour(255, 255, 0),
            "green": RGBColour(0, 255, 0),
            "blue": RGBColour(0, 0, 255),
            "indigo": RGBColour(75, 0, 130),
            "violet": RGBColour(148, 0, 211),
            "pink": RGBColour(255, 102, 178),
            "brown": RGBColour(150, 75, 0),
            "gray": RGBColour(128, 128, 128),
            "black": RGBColour(255, 255, 255),
            "white": RGBColour(0, 0, 0)
        }


    def readFromFile(self):
        coloursFile = open(self.__inFilename, "r")
        lines = coloursFile.readlines()

        for line in lines:
            if line != "\n":
                r, g, b = line.split()
                self.__colours.append(RGBColour(int(r), int(g), int(b)))

        coloursFile.close()


    def generateRandomRGBValues(self):
        coloursFile = open(self.__inFilename, "w")
        toPrint = ""
        for counter in range(50):
            for colour in range(3):
                toPrint += str(randint(0, 250)) + " "
            toPrint += "\n"
        coloursFile.write(toPrint)
        coloursFile.close()


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
            else:
                if currentColourDistance == minColourDistance:
                    similarBasicColour.append(colour)

        return similarBasicColour


    def getSimilarMainColors(self):
        for colour in self.__colours:
            self.__similarMainColors[colour] = self.getSimilarBasicColour(colour)


    def findClosestComplimentaryColours(self, colour):
        complimentaryColour = colour.getComplimentaryColor()
        similarComplimentaryBasicColour = self.getSimilarBasicColour(complimentaryColour)
        allComplimentaryColours = []
        for colour in self.__colours:
            if self.__similarMainColors[colour] == similarComplimentaryBasicColour:
                allComplimentaryColours.append(colour)

        return allComplimentaryColours, similarComplimentaryBasicColour


    def matchColours(self):
        self.getSimilarMainColors()
        for colour in self.__colours:
            matches, mainComplimenataryColor = self.findClosestComplimentaryColours(colour)
            self.__matches[colour] = matches

    def buildMatchPair(self):
        pairs = []
        for colour in self.__matches.keys():
            for matchingColour in self.__matches[colour]:
                if [matchingColour, colour]  not in pairs:
                    pairs.append([colour, matchingColour])
        return pairs


    def writeToFile(self, outFilename):
        pairs = self.buildMatchPair()
        outFile = open(outFilename, "w")
        toPrint = ""
        for pair in pairs:
            toPrint += "shade of " + str(self.__similarMainColors[pair[0]][0]) + ": " + str(pair[0]) +\
                       " + shade of " + str(self.__similarMainColors[pair[1]][0]) + ": " + str(pair[1]) + "\n"

        outFile.write(toPrint)
        outFile.close()





