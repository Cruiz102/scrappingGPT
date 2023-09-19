from PIL import Image, ImageDraw
import pytesseract
from pytesseract import Output

# Load the image
image = Image.open('images/screenshot.png')

# Use pytesseract to extract word bounding boxes
data = pytesseract.image_to_data(image, output_type=Output.DICT)

# Prepare for drawing on the image
draw = ImageDraw.Draw(image)

found_send_image = False

# Draw bounding boxes around detected words
for i in range(len(data['text'])):
    if data['text'][i].strip() != '':
        word = data['text'][i]
        left, top, width, height = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        
        # Draw the bounding box
        draw.rectangle(((left, top), (left+width, top+height)), outline='red')
        
        # Check if the word matches "Send Image"
        if word == "Senda":
            found_send_image = True

# Save the image with bounding boxes
image.save('images/output_image_with_boxes.png')

if found_send_image:
    print("'Send Image' was found in the image!")
else:
    print("'Send Image' was not found in the image.")