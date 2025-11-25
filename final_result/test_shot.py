from ultralytics import YOLO
import cv2


model = YOLO("./train22/weights/best.pt")  # change par ton chemin


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra")
    exit()

print("Appuie sur 's' pour prendre un screenshot et le traiter.")
print("Appuie sur 'q' pour quitter.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if key == ord('s'):
        screenshot = frame.copy()

        results = model(screenshot)

        print("\n--- CLASSES DÉTECTÉES ---")
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls)
                class_name = model.names[cls_id]
                conf = float(box.conf)
                print(f"Classe : {class_name} | confiance = {conf:.2f}")

        annotated = results[0].plot()

        cv2.imshow("Screenshot traité", annotated)


cap.release()
cv2.destroyAllWindows()
