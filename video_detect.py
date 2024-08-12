from ultralytics import YOLO
import cv2
import math

def video_detection(path_x):
    video_capture = path_x
    cap = cv2.VideoCapture('C:\\Users\\Desktop\\ppe mini project\\videos\\demo.mp4')

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the output dimensions (you can adjust these values)
    out_width = 200  # New width
    out_height = 200  # New height

    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (out_width, out_height))

    model = YOLO(r'C:\Users\Desktop\ppe mini project\best.pt') 

    classNames = ["Protective Helmet", "Face Shield", "Jacket", "Dust Mask", "Eye Wear", "Glove", "Protective Boots"]

    while True:
        success, img = cap.read()
        
        # Resize the frame to the desired output dimensions
        img = cv2.resize(img, (out_width, out_height))
        
        # Doing detections using YOLOv8 frame by frame
        results = model(img, stream=True)

        # Loop through and process the results...
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
        yield img
        #out.write(img)
        #cv2.imshow("Image", img)
        
        #if cv2.waitKey(1) & 0xFF == ord('1'):
        #    break

    #out.release()
    cap.release()
    cv2.destroyAllWindows()
