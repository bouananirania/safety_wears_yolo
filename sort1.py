import os
import shutil

# Chemin de ton dossier principal où se trouvent les dossiers 0,1,2,...,14
root_dir = "./sorted"   # <<< change ici

# Extensions considérées comme images
image_ext = {".jpg", ".jpeg", ".png"}

for i in range(15):  # dossiers 0 à 14
    folder_path = os.path.join(root_dir, str(i))

    if not os.path.isdir(folder_path):
        print(f"❌ Le dossier {folder_path} n'existe pas, je passe.")
        continue

    # Créer images/ et labels/
    images_dir = os.path.join(folder_path, "images")
    labels_dir = os.path.join(folder_path, "labels")

    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(labels_dir, exist_ok=True)

    # Parcourir les fichiers du dossier
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # ignorer les dossiers qu'on vient de créer
        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()

        if ext in image_ext:
            shutil.move(file_path, os.path.join(images_dir, file))
        elif ext == ".txt":
            shutil.move(file_path, os.path.join(labels_dir, file))

    print(f"✔ Dossier {i} traité.")

print("🎉 Séparation terminée !")
