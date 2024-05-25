import cv2
import easyocr
import os

def perform_ocr(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    # Get the list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # Read the input image
        image_path = os.path.join(input_folder, image_file)
        original_image = cv2.imread(image_path)

        # Perform OCR on the image
        results = reader.readtext(original_image)

        # Draw red boxes with green-colored OCR text
        for (bbox, text, prob) in results:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))

            # Draw a red box
            cv2.rectangle(original_image, top_left, bottom_right, (0, 0, 255), 2)

            # Draw green-colored OCR text beside the red box
            cv2.putText(original_image, text, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save the output image to the output folder
        output_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_output.png")
        cv2.imwrite(output_path, original_image)

if __name__ == "__main__":
    input_folder = "C:\\Users\\Sachin\\Downloads\\License Images.zip-20240203T142247Z-001\\License Images"  # Replace with the actual path to the input folder
    output_folder = "C:\\Users\\Sachin\\Downloads\\License Images.zip-20240203T142247Z-001\\License Outputs"  # Output folder where the processed images will be saved

    perform_ocr(input_folder, output_folder)
