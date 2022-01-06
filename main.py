from Repositorys.ImageRepository import ImageRepository
from Services.LedService import LedService
# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    imr = ImageRepository('Resource/TV_TEST_PLAIN_170MM.jpg')
    ledServ = LedService()
    ledServ.show()
    imr.tvSetup()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main('Resource/tv_sample.jpeg')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
