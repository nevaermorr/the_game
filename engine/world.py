from engine.generalFunctions import *


class World:
    """
    class representing the world
    """
    #boolean flag ending the game
    gameOver = False

    def __init__(self):
        """
        creation of the world!
        """
        from engine.time import Time

        #initialize some environment
        self.createEnvironment()
        #starting the great clock
        self.time = Time()

    def run(self):
        """
        main loop running the game
        """
        while not World.gameOver:
            #time flies
            self.time.passTime()
            #we are giving a chance to act for everything that is eligible for acting
            for animate in self.currentLocation.getAnimates():
                animate.act()
                #no point in letting anyone act if the game is over
                if World.gameOver:
                    break
            #temporary doomsday established to prevent the game from running infinitely
            if self.time.dayCount == 10:
                break
        #game over here
        else:
            self.endGame()

    def endGame(self):
        """
        indicate end of the game for the World.run() method
        """
        log('msg', 'nothing to do here...')
        log('msg', self.time.getCurrentTime())

    def createEnvironment(self):
        """
        create some environment for testing purposes
        """
        from engine.map import Map
        from engine.hero import Hero

        #a single map will do for now
        self.maps_ = [Map()]
        #pointer to current location
        self.currentLocation = self.maps_[0]

        log('msg', 'a hero is born')
        hero = Hero(self.currentLocation, [0, 0])