import os
import shutil

src_root = "./sorted"          # dossier original
dst_root = "./sorted_limited"      # dossier résultat
max_images = 800               # limite par classe

# 1️⃣ Copier entièrement sorted → sorted_new
if os.path.exists(dst_root):
    print("⚠️ Le dossier sorted_new existe déjà. Supprime-le ou change le nom.")
    exit()

print("📂 Copie du dossier entier...")
shutil.copytree(src_root, dst_root)
print("✔ Copie terminée !")

# 2️⃣ Nettoyage dans sorted_new (pas dans sorted)
for i in range(15):
    folder_path = os.path.join(dst_root, str(i))
    images_dir = os.path.join(folder_path, "images")
    labels_dir = os.path.join(folder_path, "labels")

    if not os.path.isdir(images_dir) or not os.path.isdir(labels_dir):
        print(f"❌ Dossier {i} incomplet, je passe.")
        continue

    # Liste des images triées
    images = sorted([
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".png", ".jpeg"))
    ])

    print(f"Dossier {i} : {len(images)} images trouvées")

    if len(images) > max_images:
        to_delete = images[max_images:]  # celles à supprimer

        for img in to_delete:
            img_path = os.path.join(images_dir, img)
            os.remove(img_path)

            # supprimer le label associé
            txt_name = os.path.splitext(img)[0] + ".txt"
            txt_path = os.path.join(labels_dir, txt_name)

            if os.path.exists(txt_path):
                os.remove(txt_path)

        print(f"🗑 {len(to_delete)} images supprimées dans dossier {i}")

    else:
        print(f"✔ Dossier {i} OK (≤ 800 images)")

print("🎉 sorted_new est prêt ! Aucune modification sur sorted original.")
