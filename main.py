#from Repositorys.ImageRepository import ImageRepository
from Services.LedService import LedService
import time
# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    #imr = ImageRepository('Resource/TV_TEST_PLAIN_170MM.jpg')
    ledServ = LedService()
    ledServ.lightSingleLed(0, [255,255,255])
    time.sleep(1)
    ledServ.lightAllLed([0,0,0])
    ledServ.lightSingleLed(1, [255,0,0])
    time.sleep(1)
    ledServ.lightAllLed([0,0,0])
    ledServ.lightSingleLed(2, [0,255,0])
    time.sleep(1)
    ledServ.lightAllLed([0,0,0])
    ledServ.lightSingleLed(3, [0,0,255])
    time.sleep(1)
    ledServ.lightAllLed([0,0,0])
    #imr.tvSetup()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main('Resource/tv_sample.jpeg')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
