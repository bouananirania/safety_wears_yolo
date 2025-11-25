import os

def analyze_labels(split_path):
    labels_dir = os.path.join(split_path, "labels")

    det_only = 0
    seg_only = 0
    det_and_seg = 0

    for txt in os.listdir(labels_dir):
        if not txt.endswith(".txt"):
            continue

        txt_path = os.path.join(labels_dir, txt)
        has_det = False
        has_seg = False

        with open(txt_path, "r") as f:
            for line in f:
                parts = line.strip().split()

                # bbox = 5 valeurs
                if len(parts) == 5:
                    has_det = True

                # segmentation = plus que 5 valeurs
                elif len(parts) > 5:
                    has_seg = True

        # Classification du fichier
        if has_det and not has_seg:
            det_only += 1
        elif has_seg and not has_det:
            seg_only += 1
        elif has_det and has_seg:
            det_and_seg += 1

    print(f"📁 {os.path.basename(split_path)}")
    print(f"🔵 Détection seulement       : {det_only}")
    print(f"🟣 Segmentation seulement    : {seg_only}")
    print(f"🟡 Mix (det + seg)           : {det_and_seg}")
    print("-" * 40)


# Analyse des trois dossiers
dataset_root = "./dataset_limited2"   # <<< change ici

for split in ["train", "valid", "test"]:
    split_dir = os.path.join(dataset_root, split)
    
    if not os.path.isdir(split_dir):
        print(f"⚠️ Dossier {split} introuvable.")
        continue
    
    analyze_labels(split_dir)
