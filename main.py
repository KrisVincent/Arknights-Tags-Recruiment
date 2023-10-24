from PIL import Image
#import pytesseract
import numpy as np
from ImageProcessor import ImageProcessor
from RhodesAPIClient import RhodesAPIClient

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
process_image = ImageProcessor()

filename = 'Arknights.jpg'
process_image.set_screenshot(filename)
process_image.process_screenshot()
 

api_client = RhodesAPIClient()
api_client.set_query_param("tags", "Guard")
api_client.set_query_param("recruitable", "Yes")
api_client.set_query_param("rarity", "6")
api_client.get_recruitments()
 

img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)

 
