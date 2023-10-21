from PIL import Image
import pytesseract
import numpy as np
from ImageProcessor import ImageProcessor

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


process_image = ImageProcessor()



filename = 'Arknights.jpg'
process_image.set_screenshot(filename)
process_image.process_screenshot()


img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)