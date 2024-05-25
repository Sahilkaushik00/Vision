import cv2
import rembg
import numpy as np

def main():

    input_path = "C:\\Users\\Sachin\\Downloads\\TEST IMAGES-20240202T165027Z-001\\TEST IMAGES"

    image_names = ["1.jpg", "2.jpg"]  

    for image_name in image_names:
        image_path = f"{input_path}/{image_name}"

        
        image = cv2.imread(image_path)
       
        if image is None:
            print(f"Error reading image: {image_path}")
            continue

       
        # Resizing the image to fit the screen
        original_image = cv2.resize(image, (800, 600))  # Adjust dimensions as needed
        cv2.imshow("Original Image", original_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        while True:
            
            roi = cv2.selectROI(original_image)
            cv2.destroyAllWindows()

            # Croping the selected Region Of Interest (ROI)
            cropped_roi = original_image[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

            # Using rembg library to remove the background
            transparent_roi = rembg.remove(cropped_roi)

            # Draw an outline over the object
            object_outline = cv2.Canny(transparent_roi[:, :, 3], 30, 100)

            # Overlay the object outline in the original input image
            original_image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]][object_outline != 0] = [0, 255, 0]

            cv2.imshow("Object Outline", original_image)
            key = cv2.waitKey(0) & 0xFF

            # Press 'q' for next image or to exit the loop
            if key == ord('q'):
                break

            # Press 'c' to clear the outline
            elif key == ord('c'):
                original_image = cv2.imread(image_path)
                original_image = cv2.resize(image, (800, 600))  # Adjust dimensions as needed
                cv2.imshow("Original Image", original_image)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
