import cv2
import mediapipe as mp

def draw_pose(video_path, output_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    # Creating a MediaPipe Pose object
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

    while True:
        
        ret, frame = cap.read()

        if not ret:
            break

        # Converting to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Performing pose estimation
        results = pose.process(rgb_frame)

        # Drawing the skeleton on the frame
        if results.pose_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Writing the frame to the output video
        out.write(frame)

        
        cv2.imshow("Pose Estimation", frame)

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = "C:\\Users\\Sachin\\Downloads\\task_4_video.mp4-20240203T144426Z-001\\task_4_video.mp4"
    output_video_path = "C:\\Users\\Sachin\\Downloads\\task_4_video.mp4-20240203T144426Z-001\\output_task_4.mp4"

    draw_pose(input_video_path, output_video_path)
