import os

def check_split(split_path):
    images_dir = os.path.join(split_path, "images")
    labels_dir = os.path.join(split_path, "labels")

    image_exts = (".jpg", ".jpeg", ".png")

    images = [f for f in os.listdir(images_dir) if f.lower().endswith(image_exts)]
    labels = [f for f in os.listdir(labels_dir) if f.lower().endswith(".txt")]

    # enlever extensions pour comparaison
    img_names = {os.path.splitext(f)[0] for f in images}
    lbl_names = {os.path.splitext(f)[0] for f in labels}

    missing_labels = img_names - lbl_names      # image mais pas de txt
    missing_images = lbl_names - img_names      # txt mais pas d'image

    print(f"📁 {os.path.basename(split_path)}")
    print(f"Images : {len(images)} | Labels : {len(labels)}")
    print(f"❌ Images sans label : {len(missing_labels)}")
    print(f"❌ Labels sans image : {len(missing_images)}")
    print("-" * 40)

    return missing_labels, missing_images


# 🚀 Vérification principale
dataset_root = "./dataset_limited2"   # <<< change ici

for split in ["train", "valid", "test"]:
    split_dir = os.path.join(dataset_root, split)
    
    if not os.path.isdir(split_dir):
        print(f"⚠️ Dossier {split} introuvable, je passe.")
        continue
    
    check_split(split_dir)
