import os

def verify_yolo_dataset(image_folder, label_folder):
    """
    Vérifie la cohérence d'un dataset YOLO
    """
    errors = {
        "images_without_label": [],
        "txt_in_images_folder": [],
        "jpg_in_labels_folder": []
    }

    # ----------------------------
    # 1) Vérifier que chaque image a son label
    # ----------------------------
    image_files = [f for f in os.listdir(image_folder)
                   if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    for img in image_files:
        base = os.path.splitext(img)[0]
        txt_path = os.path.join(label_folder, base + ".txt")
        if not os.path.exists(txt_path):
            errors["images_without_label"].append(img)

    # ----------------------------
    # 2) Vérifier qu'il n'y a pas de .txt dans images
    # ----------------------------
    for f in os.listdir(image_folder):
        if f.lower().endswith(".txt"):
            errors["txt_in_images_folder"].append(f)

    # ----------------------------
    # 3) Vérifier qu'il n'y a pas de .jpg/.png/.jpeg dans labels
    # ----------------------------
    for f in os.listdir(label_folder):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            errors["jpg_in_labels_folder"].append(f)

    # ----------------------------
    # Résultat
    # ----------------------------
    print("\n=== VÉRIFICATION DATASET YOLO ===\n")
    if not any(errors.values()):
        print("✅ Dataset OK : toutes les images ont un label, aucun fichier incorrect trouvé.")
    else:
        if errors["images_without_label"]:
            print(f"❌ Images sans label : {len(errors['images_without_label'])} fichiers")
            for f in errors["images_without_label"]:
                print("   -", f)
        if errors["txt_in_images_folder"]:
            print(f"❌ .txt trouvés dans images : {len(errors['txt_in_images_folder'])} fichiers")
            for f in errors["txt_in_images_folder"]:
                print("   -", f)
        if errors["jpg_in_labels_folder"]:
            print(f"❌ Images trouvées dans labels : {len(errors['jpg_in_labels_folder'])} fichiers")
            for f in errors["jpg_in_labels_folder"]:
                print("   -", f)
    print("\n=== FIN VÉRIFICATION ===\n")


# -----------------------------------------------------
# 📌 UTILISATION :
# -----------------------------------------------------
verify_yolo_dataset(
    image_folder="train/images",
    label_folder="train/labels"
)
