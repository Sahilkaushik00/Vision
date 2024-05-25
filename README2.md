#Motion Detection and Tracking
This Python project detects green polka dots (either dark or light) in a video ("task_2_video.mp4") using HSV filtering and hardcoded values. It then draws a red dot at the center of each detected dot, generating an output video.

Highlights
Detects green polka dots (configurable for dark or light)
Overlays a red dot at the center of each detected dot
Processes all frames in the video
Requirements
Python (version 3.6 or later)
OpenCV library (pip install opencv-python)
Usage
Install OpenCV: Open a terminal or command prompt and run:


pip install opencv-python


Adjust the hardcoded HSV values in the code for more precise detection based on your video's color range.
Run the script: Execute the Python script containing the code.

Output
The script will generate an output video with red dots on top of the detected green polka dots.

Notes
This is a developmental project with potential for further refinement.
Consider implementing more robust color detection mechanisms if needed.
Contributing
Feel free to fork this repository and contribute improvements or enhancements!
