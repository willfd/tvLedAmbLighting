import numpy
from PIL import Image
from matplotlib import pyplot
import math
import cv2


class ImageService:
    def __init__(self):
        return

    @staticmethod
    def ConvertImageToImageObj(filepath: str):
        return Image.open(filepath)

    @staticmethod
    def ConvertImageToCVObj(filepath: str):
        return cv2.imread(filepath)

    @staticmethod
    def ReduceImageObj(image_obj, scale: float):
        obj_size = image_obj.size
        # print(f"image size: {obj_size}")
        # aspect_ratio = obj_size[0]/obj_size[1]
        # print(f"aspect ratio: {aspect_ratio}")
        new_x = int(math.ceil(obj_size[0]*scale))
        new_y = int(math.ceil(obj_size[1]*scale))
        new_image_obj = image_obj.resize((new_x, new_y), Image.ANTIALIAS)
        new_obj_size = new_image_obj.size
        print(f"image size: {new_obj_size}")
        new_aspect_ratio = new_obj_size[0]/new_obj_size[1]
        print(f"aspect ratio: {new_aspect_ratio}")
        return new_image_obj

    def ReduceMultipleImageObjs(self, image_obj, scale_list: list):
        reduced_image_objs = []
        for scale in scale_list:
            reduced_image_objs.append(self.ReduceImageObj(image_obj, scale))
        return reduced_image_objs

    @staticmethod
    def ConvertImageObjToArray(image_obj):
        return numpy.asarray(image_obj)

    @staticmethod
    def plotImgObj(array: []):
        pyplot.imshow(array)
        return pyplot.show()

    @staticmethod
    def plotCVObj(array: []):
        cv2.imshow("OPEN CV IMAGE", array)
        cv2.waitKey(0)
        return pyplot.show()

    @staticmethod
    def plotCompareCVObj(array: [], array2: []):
        cv2.namedWindow("Original")
        cv2.imshow("Original", array)
        cv2.namedWindow("Modified")
        cv2.imshow("Modified", array2)
        cv2.waitKey(0)
        return pyplot.show()

    @staticmethod
    def cvGreyScale(array: []):
        return cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def cvEdgeDetect(array: [], low_threshold: int, high_threshold: int):
        return cv2.Canny(array, low_threshold, high_threshold)

    @staticmethod
    def cvBlur(array: []):
        return cv2.GaussianBlur(array, (5, 5), 0)

    @staticmethod
    def cvColorGraph(array: []):
        r_hist = cv2.calcHist([array], [0], None, [256], [0, 256])
        g_hist = cv2.calcHist([array], [1], None, [256], [0, 256])
        b_hist = cv2.calcHist([array], [2], None, [256], [0, 256])

        pyplot.subplot(221), pyplot.imshow(array)
        pyplot.subplot(222), pyplot.plot(r_hist), pyplot.plot(g_hist), pyplot.plot(b_hist)
        pyplot.xlim([0, 256])

        pyplot.show()
        # print(hist)
        return True

    @staticmethod
    def resizeCVArray(array: [], resize_factor: float = 0):
        array_shape = array.shape
        resized = (int(array_shape[0] * resize_factor), int(array_shape[1] * resize_factor))
        return cv2.resize(array, resized, interpolation=cv2.INTER_AREA)

    @staticmethod
    def detectMostFreqColor(array: [], resize_factor: float = 0):
        """
        Analyse the inputted CV Array for the most common colored pixel that is not Black or White
        :param array: CV Array
        :param resize_factor: float < 1
        :return: STRING = Most Freq - {[R,G,B]} Occurs: {How many Times} has a mean of {mean color level}
        """

        array_shape = array.shape
        img_temp = array
        if resize_factor:
            resized = (int(array_shape[0]*resize_factor), int(array_shape[1]*resize_factor))
            img_temp = cv2.resize(array, resized, interpolation=cv2.INTER_AREA)
        unique, counts = numpy.unique(img_temp.reshape(-1, 3), axis=0, return_counts=True)
        max_count = 0
        max_pixel = []
        max_mean = 0
        unique_pixel = []
        for i in range(len(unique)):
            unique_pixel = unique[i]
            unique_pixel_mean = unique_pixel.mean()
            if not (unique_pixel_mean < 20 or unique_pixel_mean > 240):
                if counts[i] > max_count:
                    max_count = counts[i]
                    max_pixel = unique_pixel
                    max_mean = unique_pixel_mean
                # print(f"{unique_pixel} Occurs: {counts[i]}")
        print(f"Most Freq - {max_pixel} Occurs: {max_count} has a mean of {max_mean}")
        return unique_pixel

    @staticmethod
    def highlightSingleColor(array: [], pixel_color: [], margin: int):
        above_margin_check = lambda color, _pixel_color: (color - margin) < _pixel_color
        below_margin_check = lambda color, _pixel_color: (color + margin) > _pixel_color

        target_r_color = pixel_color[0]
        target_g_color = pixel_color[1]
        target_b_color = pixel_color[2]
        modified_array = array
        for row in range(len(array)):
            for cell in range(len(array[row])):
                pixel = array[row][cell]
                # print(pixel)

                pixel_r_color_in_margins = above_margin_check(target_r_color, pixel[0]) and below_margin_check(target_r_color, pixel[0])
                pixel_g_color_in_margins = above_margin_check(target_g_color, pixel[1]) and below_margin_check(target_g_color, pixel[1])
                pixel_b_color_in_margins = above_margin_check(target_b_color, pixel[2]) and below_margin_check(target_b_color, pixel[2])
                in_margin = pixel_r_color_in_margins and pixel_b_color_in_margins and pixel_g_color_in_margins
                if not in_margin:
                    modified_array[row][cell] = numpy.array([0,0,0])
                # print(modified_pixel)
                # print(type(modified_pixel))
        return modified_array

    @staticmethod
    def cvContourDetect(array: [], thresh: int, max_val: int):
        thresh = cv2.threshold(array, thresh, max_val, cv2.THRESH_BINARY)[1]
        # find contours in the threshold image and initialize the
        # shape detector
        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image=array, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        return array

    @staticmethod
    def saveArrayAsImage(array: [], save_filepath: str):
        if input("Save Array? Y/N") in ["yes", "Yes", "Y", "y"]:
            if ".png" not in save_filepath:
                if "." in save_filepath:
                    save_filepath = save_filepath.split(".")[0]
                save_filepath += ".png"

            array_image = Image.fromarray(array)
            return array_image.save(save_filepath)
        return False
