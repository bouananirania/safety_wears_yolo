from ultralytics import YOLO
import cv2


model = YOLO("./train22/weights/best.pt")   


cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Real-Time Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
