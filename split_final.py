import os
import shutil
import random

# Dossier contenant les dossiers 0 à 14
root_dir = "./sorted_limited"     # <<< change ici

# Dossier de sortie
output = "./dataset_limited"
splits = ["train", "valid", "test"]

# Préparer structure de sortie
for sp in splits:
    os.makedirs(os.path.join(output, sp, "images"), exist_ok=True)
    os.makedirs(os.path.join(output, sp, "labels"), exist_ok=True)

# Extensions images acceptées
image_ext = {".jpg", ".jpeg", ".png"}


for cls in range(15):

    class_dir = os.path.join(root_dir, str(cls))
    images_dir = os.path.join(class_dir, "images")
    labels_dir = os.path.join(class_dir, "labels")

    if not os.path.isdir(images_dir) or not os.path.isdir(labels_dir):
        print(f"❌ Classe {cls} ignorée (dossier incomplet)")
        continue

    # Trouver les paires image+label
    images = {os.path.splitext(f)[0]: f for f in os.listdir(images_dir)
              if os.path.splitext(f)[1].lower() in image_ext}

    labels = {os.path.splitext(f)[0]: f for f in os.listdir(labels_dir)
              if f.endswith(".txt")}

    # On garde seulement les correspondances
    matching = list(set(images.keys()).intersection(labels.keys()))

    # Mélanger
    random.shuffle(matching)

    # Split 80 / 10 / 10
    n = len(matching)
    n_train = int(n * 0.8)
    n_valid = int(n * 0.1)
    n_test  = n - n_train - n_valid  # reste

    split_data = {
        "train": matching[:n_train],
        "valid": matching[n_train:n_train+n_valid],
        "test":  matching[n_train+n_valid:]
    }

    print(f"Classe {cls} → total {n} | train {n_train}, valid {n_valid}, test {n_test}")

    # Copier les fichiers
    for split_name, base_names in split_data.items():

        for base in base_names:

            # Image
            img_file = images[base]
            shutil.copy(
                os.path.join(images_dir, img_file),
                os.path.join(output, split_name, "images", f"{cls}_{img_file}")
            )

            # Label
            lbl_file = labels[base]
            shutil.copy(
                os.path.join(labels_dir, lbl_file),
                os.path.join(output, split_name, "labels", f"{cls}_{lbl_file}")
            )


print("🎉 Split 80/10/10 terminé !")
print("📁 Résultat dans : ./dataset/")
