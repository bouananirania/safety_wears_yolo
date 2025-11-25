import os
import shutil
import random

# -----------------------------
# 📌 1. Chemins des datasets
# -----------------------------
SOURCE_FOLDERS = [
    "./2/glasses",
   "./2/ear protection",
    "./2/without helmet"
]

DEST = {
   "train": {
        "images": "./train2/images",
        "labels": "./train2/labels"
    },
    "val": {
        "images": "./valid2/images",
        "labels":  "./valid2/labels"
    },
    "test": {
        "images": "./test2/images",
        "labels":  "./test2/labels"
    }
}

# -----------------------------
# 📌 2. Paramètres
# -----------------------------
N_TRAIN = 500
N_VAL = 62
N_TEST = 62


# -----------------------------
# 📌 3. Fonction utilitaire
# -----------------------------
def ensure_dirs():
    """Créer les dossiers nécessaires"""
    for split in DEST.values():
        os.makedirs(split["images"], exist_ok=True)
        os.makedirs(split["labels"], exist_ok=True)


def get_image_label_pairs(folder):
    """Retourne une liste (image_path, label_path) triée"""
    files = os.listdir(folder)
    images = [f for f in files if f.lower().endswith((".jpg", ".png", ".jpeg"))]

    pairs = []
    for img in images:
        base = os.path.splitext(img)[0]
        label = base + ".txt"
        label_path = os.path.join(folder, label)

        if os.path.isfile(label_path):  # garder seulement si txt existe
            pairs.append(
                (os.path.join(folder, img), label_path)
            )
    return pairs


def copy_samples(pairs, dest_img, dest_lbl):
    """Copie les images + labels vers destination"""
    for img, lbl in pairs:
        shutil.copy(img, dest_img)
        shutil.copy(lbl, dest_lbl)


# -----------------------------
# 📌 4. Pipeline complet
# -----------------------------
ensure_dirs()

for folder in SOURCE_FOLDERS:

    print(f"\nProcessing folder: {folder}")
    pairs = get_image_label_pairs(folder)

    if len(pairs) < (N_TRAIN + N_VAL + N_TEST):
        raise ValueError(f"❌ Le dossier {folder} ne contient pas assez d’images!")

    random.shuffle(pairs)

    train_set = pairs[:N_TRAIN]
    val_set   = pairs[N_TRAIN:N_TRAIN + N_VAL]
    test_set  = pairs[N_TRAIN + N_VAL:N_TRAIN + N_VAL + N_TEST]

    print(f"  → Train: {len(train_set)}")
    print(f"  → Val: {len(val_set)}")
    print(f"  → Test: {len(test_set)}")

    # Copier
    copy_samples(train_set, DEST["train"]["images"], DEST["train"]["labels"])
    copy_samples(val_set, DEST["val"]["images"], DEST["val"]["labels"])
    copy_samples(test_set, DEST["test"]["images"], DEST["test"]["labels"])

print("\n✅ Terminé ! Les images et labels ont été copiés correctement.")
