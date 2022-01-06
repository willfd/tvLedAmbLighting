from Services.LedService import LedService
import time


class LedRepository:
    def __init__(self):
        self.ledServ = LedService()

    def Flow(self):
        self.ledServ.blinkSingleLed(0, [255, 255, 255], 0.05)
        self.ledServ.blinkSingleLed(1, [255, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(2, [255, 0, 0], 0.05)
        self.ledServ.blinkSingleLed(3, [0, 255, 0], 0.05)
        self.ledServ.blinkSingleLed(4, [0, 0, 255], 0.05)
        
        self.ledServ.lightSingleLed(5, [125, 125, 255])
        time.sleep(0.1)
        self.ledServ.turnOffAllLed()
        self.ledServ.lightSingleLed(6, [125, 125, 125])
        time.sleep(0.1)
        self.ledServ.turnOffAllLed()
