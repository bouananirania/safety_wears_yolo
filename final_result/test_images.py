from ultralytics import YOLO
import cv2


model = YOLO("./train22/weights/best.pt")  


image_path = "i1.jpg"   


results = model(image_path)

for r in results:
    for box in r.boxes:
        cls_id = int(box.cls)
        class_name = model.names[cls_id]
        conf = float(box.conf)
        print(f"Classe : {class_name} - Confiance : {conf:.2f}")


annotated_img = results[0].plot()  

cv2.imshow("Resultat", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("resultat.jpg", annotated_img)
