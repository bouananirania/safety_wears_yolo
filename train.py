from ultralytics import YOLO
from ultralytics.data.utils import check_det_dataset

if __name__ == '__main__':
    # Vérifier le dataset
    check_det_dataset("D:/programation/python/chiali tubes/data.yaml")

    # Charger le modèle
    model = YOLO("yolov8n.pt")  # ou yolov8s.pt
    #model = YOLO("yolov8n-seg.pt")

    # Entraînement
    model.train(
        data="./data.yaml",
        epochs=30,
        imgsz=640,
        batch=8,
        amp=False,
        workers=4,   # tu peux mettre >0 maintenant
        device="cpu"   # GPU ou CPU
    )
