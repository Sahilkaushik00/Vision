import cv2
import numpy as np

def draw_red_dot_on_green_polka_dots(video_path, output_path):
   
    cap = cv2.VideoCapture(video_path)


    if not cap.isOpened():
        print("Error opening video file")
        return

    # Defined HSV range for green color
    lower_green = np.array([40, 40, 40]) 
    upper_green = np.array([80, 255, 255])

    # Creating VideoWriter object to save the output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

    while True:
        
        ret, frame = cap.read()

        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Creating a mask to extract the green polka dots
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Finding out contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Drawing a red dot at the center of each green polka dot
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        out.write(frame)
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()

    cv2.destroyAllWindows()

input_video_path = "C:\\Users\\Sachin\\Downloads\\task_2_video.mp4-20240203T132727Z-001\\task_2_video.mp4"
output_video_path = "C:\\Users\\Sachin\\Downloads\\task_2_video.mp4-20240203T132727Z-001\\output_task_2.mp4"

# Calling the function to draw red dots on green polka dots
draw_red_dot_on_green_polka_dots(input_video_path, output_video_path)
