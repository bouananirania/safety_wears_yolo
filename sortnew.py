import os
import shutil

# Dossier TRAIN contenant images/ et labels/
train_dir = "./test"   # <<< change ici

images_dir = os.path.join(train_dir, "images")
labels_dir = os.path.join(train_dir, "labels")

# Classes que tu veux extraire
target_classes = {"0", "2", "4", "8","9"}

# Dossier output
output_root = "output_classes"  # <<< il sera créé automatiquement
os.makedirs(output_root, exist_ok=True)

# Parcourir tous les fichiers .txt
for txt_file in os.listdir(labels_dir):
    if not txt_file.endswith(".txt"):
        continue

    txt_path = os.path.join(labels_dir, txt_file)

    # Lire la première ligne pour détecter la classe
    with open(txt_path, "r") as f:
        first_line = f.readline().strip()

    if not first_line:
        continue

    label_class = first_line.split()[0]  # première valeur = classe

    # Vérifier si c'est une classe cible
    if label_class in target_classes:

        # Créer dossiers pour cette classe
        class_label_dir = os.path.join(output_root, label_class, "labels")
        class_image_dir = os.path.join(output_root, label_class, "images")
        os.makedirs(class_label_dir, exist_ok=True)
        os.makedirs(class_image_dir, exist_ok=True)

        # Copier le fichier txt
        shutil.copy(txt_path, os.path.join(class_label_dir, txt_file))

        # Associer l’image portant le même nom
        base_name = os.path.splitext(txt_file)[0]

        # Chercher une image avec n’importe quelle extension
        for ext in [".jpg", ".jpeg", ".png"]:
            img_path = os.path.join(images_dir, base_name + ext)
            if os.path.exists(img_path):
                shutil.copy(img_path, os.path.join(class_image_dir, base_name + ext))
                break

        print(f"Class {label_class} → {txt_file} traité.")

print("🎉 Extraction terminée !")
