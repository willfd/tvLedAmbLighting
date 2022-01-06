from Repositorys.LedRepository import LedRepository
# from Services.LedService import LedService
# from Repositorys.ImageRepository import ImageRepository


def main():
    #imr = ImageRepository('Resource/TV_TEST_PLAIN_170MM.jpg')
    lr = LedRepository()
    lr.Flow()
    #imr.tvSetup()


if __name__ == '__main__':
    # main('Resource/tv_sample.jpeg')
    main()
