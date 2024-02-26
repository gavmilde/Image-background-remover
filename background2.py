import cv2
import numpy as np
from rembg import remove
from PIL import Image
import io


def remove_background(input_img_path, output_img_path):
    with open(input_img_path, 'rb') as img_file:
        img = img_file.read()
        output = remove(img)
        img = Image.open(io.BytesIO(output))
        img = img.convert("RGB")
        
        img.save(output_img_path, format = 'png')


# Call the function
remove_background('/Users/hamid/Documents/GitHub/Image-background-remover/istockphoto-1410538853-170667a.webp', '/Users/hamid/Downloads/kai2.jpg')