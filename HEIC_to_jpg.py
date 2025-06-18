import os
from PIL import Image
import pillow_heif

# Pfad zum Ordner mit den HEIC-Dateien (anpassen!)
input_folder = r'C:\Users\Pascal Kraus\Downloads\Photos'

# Zielordner anlegen (falls nicht vorhanden)
output_folder = os.path.join(input_folder, 'converted')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Durchsuche alle Dateien im input_folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.heic'):
        heic_path = os.path.join(input_folder, filename)
        try:
            # Lese die HEIC-Datei
            heif_file = pillow_heif.read_heif(heic_path)
            # Erstelle ein Pillow-Image aus den Rohdaten
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            # Neuen Dateinamen mit .jpg Endung festlegen
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            output_path = os.path.join(output_folder, new_filename)
            # Bild als JPEG speichern
            image.save(output_path, "JPEG")
            print(f"Konvertiert: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Fehler beim Konvertieren von {filename}: {e}")
fghfghfgh