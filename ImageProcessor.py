import cv2
import numpy as np

class ImageProcessor:

    # Constants
    WIDTH_MIN = 200
    WIDTH_MAX = 225
    HEIGHT_MIN = 60
    HEIGHT_MAX = 80
    Y_MIN = 520

    def __init__(self) -> None:

        # Initialize Properties
        self.__screenshot = None
        self.__contours = [] 

    # Set screenshot
    def set_screenshot(self, screenshot):
        self.__screenshot = screenshot

    # Set contours
    def set_contours(self, contours):
        self.__contours = contours

    # Get screenshot
    @property
    def screenshot(self):
        return self.__screenshot
    
    # Get Contours
    @property
    def contours(self):
        return self.__contours


    def process_screenshot(self):
        """
        Process the screenshot to find contours based on specific conditions.
        """

        # Set variables
        captured_contours = []

        # Get image
        img = cv2.imread(self.screenshot)

        if self.screenshot is None:
            print("Set Screenshot first")

        # Convert colored to gray scaled image
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply threshing
        ret, thresh = cv2.threshold(gray_image, 95, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) 

        # Apply Opening
        kernel = np.ones((5,5),np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # Get Contours
        contours = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        # Loop through the contours
        for c in contours:
            x,y,w,h = cv2.boundingRect(c)

            # Check your conditions
            if self.WIDTH_MIN < w < self.WIDTH_MAX and self.HEIGHT_MIN < h < self.HEIGHT_MAX and y > self.Y_MIN:
                # Append contours
                captured_contours.append(c)

        # Pass to contour property
        self.set_contours(captured_contours)

        # Draw contours
        self.draw_contours(img)

    # Draw Contours
    def draw_contours(self, image):

        for contour in self.contours:

            x, y, w, h = cv2.boundingRect(contour)

            # Draw Contours
            result = cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 5)

        self._display_image(result)

    # Debugging purposes
    def _display_image(self, image, windows_title = "Debug", scale_percent = 50):

        width1 = int(image.shape[1] * scale_percent / 100)
        height1 = int(image.shape[0] * scale_percent / 100)
        dim = (width1, height1)
        
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow(windows_title,resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
