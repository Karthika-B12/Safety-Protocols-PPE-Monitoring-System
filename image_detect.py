from ultralytics import YOLO
import cv2
model=YOLO('best.pt')
results = model("C:\\Users\\Desktop\\ppe mini project\\images\\1.jpg", show=True, conf=0.45)
cv2.waitKey(0)