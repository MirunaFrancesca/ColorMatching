from colormath.color_objects import LabColor

from Controller import Controller
from LabColour import LabColour
from RGBColour import RGBColour


if __name__ == '__main__':
    myController = Controller("Colours.in")
    # myRGB = RGBColour(62, 223, 190)
    # labColour = LabColour(100, -128, -128)
    # color1 = LabColor(lab_l=labColour.getL(), lab_a=labColour.getA(), lab_b=labColour.getB())
    # print(color1)
    # print(labColour)
    # print(labColour.computeDeltaE(LabColour(100, 128, 128)))
    myController.generateRandomRGBValues()
    myController.readFromFile()
    myController.matchColours()
    myController.writeToFile("Colours.out")


