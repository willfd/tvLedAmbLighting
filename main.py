from Repositorys.LedRepository import LedRepository
# from Services.LedService import LedService
# from Repositorys.ImageRepository import ImageRepository


def main():
    #imr = ImageRepository('Resource/TV_TEST_PLAIN_170MM.jpg')
    lr = LedRepository()
    # lr.Flow()
    # lr.Rainbow(100, 0.01)
    lr.Bouncer(10, [255, 0, 0], 0.01)
    # lr.Check(2, 2)
    #imr.tvSetup()


if __name__ == '__main__':
    # main('Resource/tv_sample.jpeg')
    main()
