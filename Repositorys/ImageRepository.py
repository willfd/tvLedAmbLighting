from Services.ImageService import ImageService


class ImageRepository:
    def __init__(self, file_path):
        self.ims = ImageService()
        self.file_path = file_path

    def tvSetup(self):
        ims = ImageService()
        # im_obj = ims.ConvertImageToImageObj(filepath)
        # ims.plotImgObj(im_obj)
        im_obj_og = ims.ConvertImageToCVObj(self.file_path)
        # ims.plotCVObj(im_obj_og)
        # ims.detectMostFreqColor(im_obj_og, 0.1)

        im_obj = ims.resizeCVArray(im_obj_og, 0.25)
        modified_img = ims.highlightSingleColor(im_obj, [76, 100, 58], 80)
        # modified_img = ims.highlightSingleColor(im_obj_og, [119, 172, 143], 80)
        # ims.plotCVObj(modified_img)
        print("still working")
        # ims.plotCompareCVObj(im_obj_og, modified_img)
        # im_hist = ims.detectMajorityColor(im_obj)

        im_obj_gry = ims.cvGreyScale(modified_img)
        im_tv_edge = ims.cvEdgeDetect(im_obj_gry, 0, 160)
        ims.plotCVObj(im_tv_edge)
