import os

# Chemin vers le dossier contenant les fichiers .txt
labels_folder = "D:/programation/python/chiali tubes/dataset_limited2/test/labels"

# Parcours tous les fichiers .txt du dossier
for filename in os.listdir(labels_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(labels_folder, filename)
        
        with open(file_path, "r") as f:
            lines = f.readlines()
        
        # Supprimer les doublons et garder l'ordre
        unique_lines = list(dict.fromkeys([line.strip() for line in lines]))
        
        # Réécrire le fichier sans doublons
        with open(file_path, "w") as f:
            for line in unique_lines:
                f.write(line + "\n")

print("Nettoyage terminé ! Tous les doublons ont été supprimés.")
