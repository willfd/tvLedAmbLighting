from Services.LedService import LedService
import time


class LedRepository:
    def __init__(self):
        self.ledServ = LedService()

    def Flow(self):
        self.ledServ.lightSingleLed(0, [255, 255, 255])
        time.sleep(1)
        self.ledServ.turnOffAllLed()
        self.ledServ.lightSingleLed(1, [255, 0, 0])
        time.sleep(1)
        self.ledServ.turnOffAllLed()
        self.ledServ.lightSingleLed(2, [0, 255, 0])
        time.sleep(1)
        self.ledServ.turnOffAllLed()
        self.ledServ.lightSingleLed(3, [0, 0, 255])
        time.sleep(1)
        self.ledServ.turnOffAllLed()