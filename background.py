import os
from rembg import remove
import cv2
import numpy as np

def remove_background(input_image_path, output_image_path):
    # Read the input image
    input_image = cv2.imread(input_image_path)
    if input_image is None:
        print(f"Could not read the input image: {input_image_path}")
        return

    # Convert the image to bytes
    input_image_bytes = cv2.imencode('.png', input_image)[1].tobytes()

    # Remove the background
    output_image_bytes = remove(input_image_bytes)

    # Convert bytes back to image
    output_image = cv2.imdecode(np.frombuffer(output_image_bytes, np.uint8), cv2.IMREAD_UNCHANGED)
    if output_image is None:
        print("Could not decode the output image from bytes.")
        return

    # Ensure output directory exists, if not print an error message
    output_dir = os.path.dirname(output_image_path)
    if output_dir and not os.path.exists(output_dir):
        print(f"The output directory does not exist: {output_dir}")
        return

    # Save the output image
    try:
        cv2.imwrite(output_image_path, output_image)
        print(f"Output image saved successfully: {output_image_path}")
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")

def main():
    # Prompt the user for the input and output image paths
    input_image_path = input("Enter the path to the input image: ").strip()
    output_image_path = input("Enter the path to save the output image and the image name: ").strip()

    # Normalize the file extension to ensure OpenCV recognizes it
    filename, file_extension = os.path.splitext(output_image_path)
    if file_extension.lower() not in ['.jpg', '.jpeg', '.png', '.bmp']:
        output_image_path = f"{filename}.png"  # Default to .png if extension is unrecognized

    print(f"Using output image path: {output_image_path}")
    
    # Remove the background from the input image
    remove_background(input_image_path, output_image_path)

if __name__ == "__main__":
    main()