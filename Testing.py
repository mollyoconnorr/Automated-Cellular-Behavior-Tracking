import cv2
import os

# Step 1: Crop the video
video_path = "example_of_deciliation.mp4"
cropped_video_path = "cropped_video.mp4"
x, y, w, h = 243, 205, 1433, 799

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(cropped_video_path, fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cropped_frame = frame[y:y+h, x:x+w]
    out.write(cropped_frame)

cap.release()
out.release()

frame_output_folder = "/Users/newuser_1/Desktop/Internship/PythonProject/InputImages"
# Step 2: Extract frames from cropped video
os.makedirs(frame_output_folder, exist_ok=True)

cap = cv2.VideoCapture(cropped_video_path)
frame_number = 0;
while True:
    print("CAPTURING FRAMES, DO NOT CLOSE PROJECT")
    print("Please wait until you receive the 'COMPLETE' message")

    ret, frame = cap.read()
    if not ret:
        break
    frame_path = os.path.join(frame_output_folder, f"frame_{frame_number:04d}.png")
    cv2.imwrite(frame_path, frame)
    frame_number += 1

cap.release()
print("COMPLETE")

print(f"Saved {frame_number} frames to {frame_output_folder}")