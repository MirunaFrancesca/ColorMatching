from Controller import Controller
from RGBColour import RGBColour


if __name__ == '__main__':
    myController = Controller("Colours.in")
    myController.readFromFile()
    myController.matchColours()
    myController.writeToFile("Colours.out")


