# USED TO FIND DIMENSIONS OF VIDEO TO TRACK
import cv2

# Path to your video
video_path = "example_of_deciliation.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)

# Read the first frame to select ROI
ret, frame = cap.read()
if not ret:
    print("Cannot read video")
    cap.release()
    exit()

# Let user manually select the region
r = cv2.selectROI("Select ROI", frame, showCrosshair=True, fromCenter=False)
x, y, w, h = r
print(f"Selected region - x: {x}, y: {y}, width: {w}, height: {h}")

# Optional: show the cropped region
cropped = frame[y:y+h, x:x+w]
cv2.imshow("Cropped Frame", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap.release()
