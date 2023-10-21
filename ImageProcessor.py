import cv2
import numpy as np

class ImageProcessor:
    def __init__(self) -> None:
        self.__screenshot = None

    def set_screenshot(self, screenshot):
        self.__screenshot = screenshot

    @property
    def screenshot(self):
        return self.__screenshot

    def process_screenshot(self):

        # Check if screenshot has been set
        if self.screenshot is None:
            print("Set Screenshot first")

        # Get image
        img = cv2.imread(self.screenshot)

        # Convert colored to gray scaled image
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply threshing
        ret, thresh = cv2.threshold(gray_image, 95, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) 

        # Display thresh
        self._display_image(thresh)

        # Apply Opening
        kernel = np.ones((5,5),np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # Display thresh
        self._display_image(opening)


    # Debugging purposes
    def _display_image(self, image, windows_title = "Debug", scale_percent = 50):

        width1 = int(image.shape[1] * scale_percent / 100)
        height1 = int(image.shape[0] * scale_percent / 100)
        dim = (width1, height1)
        
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow(windows_title,resized)
        cv2.waitKey(0)