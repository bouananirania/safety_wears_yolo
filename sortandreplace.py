import os
import shutil

# Dossier TRAIN contenant images/ et labels/
train_dir = "./train"  # <<< change ici

images_dir = os.path.join(train_dir, "images")
labels_dir = os.path.join(train_dir, "labels")

# Classes que tu veux garder
target_classes = {"0", "2", "4", "8", "9"}

# Remplacement
replace_map = {
    "2": "1",
    "0": "6",
    "9": "7",
    "4": "13",
    "8": "14"
}

# dossier de sortie
output_root = "output_classes"
os.makedirs(output_root, exist_ok=True)

for txt_file in os.listdir(labels_dir):

    if not txt_file.endswith(".txt"):
        continue

    txt_path = os.path.join(labels_dir, txt_file)

    with open(txt_path, "r") as f:
        lines = f.readlines()

    filtered_lines = []

    # garder seulement les lignes dont la classe est dans target_classes
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 0:
            continue

        cls = parts[0]

        if cls in target_classes:
            filtered_lines.append(parts)  # garder en parts

    # si aucune ligne conservée → ignorer complètement
    if len(filtered_lines) == 0:
        print(f"❌ Aucune classe utile dans : {txt_file}")
        continue

    # Remplacement classes
    new_lines = []
    new_classes = []

    for parts in filtered_lines:
        old_cls = parts[0]
        new_cls = replace_map[old_cls]   # remplacement
        parts[0] = new_cls
        new_classes.append(new_cls)
        new_lines.append(" ".join(parts) + "\n")

    # La classe finale utilisée pour ranger le fichier
    final_class = new_classes[0]

    class_label_dir = os.path.join(output_root, final_class, "labels")
    class_image_dir = os.path.join(output_root, final_class, "images")
    os.makedirs(class_label_dir, exist_ok=True)
    os.makedirs(class_image_dir, exist_ok=True)

    # Sauvegarder le label modifié
    out_label_path = os.path.join(class_label_dir, txt_file)
    with open(out_label_path, "w") as f:
        f.writelines(new_lines)

    # Copier l'image correspondante
    base = os.path.splitext(txt_file)[0]
    copied_image = False

    for ext in [".jpg", ".jpeg", ".png"]:
        img_path = os.path.join(images_dir, base + ext)
        if os.path.exists(img_path):
            shutil.copy(img_path, os.path.join(class_image_dir, base + ext))
            copied_image = True
            break

    print(f"✔ {txt_file} traité → Classe finale : {final_class}")

print("\n🎉 Traitement terminé !")
