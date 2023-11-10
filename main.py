import requests
from ImageProcessor import ImageProcessor
from RhodesAPIClient import RhodesAPIClient
from OCRProcessor import OCRProcessor

TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
FILENAME = 'Arknights.jpg'
 
def process_image(filename):

  process_image = ImageProcessor()
  ocr_processor = OCRProcessor(TESSERACT_CMD)

  # Process screenshot and get text
  process_image.set_screenshot(filename)
  process_image.process_screenshot()

  # Grab the processed image for text detection
  processed_images = process_image.images 

  # Detect and clean Text
  tags = [ocr_processor.perform_ocr(image).replace(':', '').replace('\n', '').strip() for image in processed_images]
  cleaned_tags = [tag for tag in tags if tag]

  return cleaned_tags

def get_recruitments(api_client, tags_to_process):
  # Declare a dictionary
  recruitable_operators = dict()

  # Loop through individual tags and combinations
  for tag in tags_to_process:
      
      # Get request
      operators = api_client.get_recruitments(tag)

      # Add to our dicitonary
      for name, data in operators.items():
        recruitable_operators[name] = recruitable_operators.get(name, data)

  # Return recruitable operators
  return recruitable_operators
   

if __name__ == '__main__':
    
    process_image_result = process_image(FILENAME)
    recruitable_operators = get_recruitments(api_client=RhodesAPIClient(), tags_to_process=process_image_result)

    response = requests.post("http://192.168.3.60:5000/recruit/data", json=recruitable_operators)

    print(response.status_code)
