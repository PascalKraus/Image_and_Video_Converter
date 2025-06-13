#Doesnt really work i guess :/

import os
import subprocess

# Pfad zum Ordner mit den MOV-Dateien
input_folder = r'C:\Users\Pascal Kraus\Downloads\Photos'

# Zielordner "converted_mov" anlegen (falls nicht vorhanden)
output_folder = os.path.join(input_folder, 'converted_mov')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Durchlaufe alle Dateien im input_folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.mov'):
        mov_path = os.path.join(input_folder, filename)
        # Ersetze die Dateiendung .mov durch .mp4
        new_filename = os.path.splitext(filename)[0] + '.mp4'
        output_path = os.path.join(output_folder, new_filename)
        
        # ffmpeg-Befehl: Konvertierung mit H.264-Codec für Video und AAC für Audio
        command = [
            'ffmpeg',
            '-i', mov_path,
            '-c:v', 'libx264',
            '-preset', 'slow',    # wahlweise: ultrafast, superfast, veryfast, faster, fast, medium (Standard), slow, veryslow
            '-crf', '22',         # Qualitätsfaktor (0 = verlustfrei, 23 = Standard; kleinere Werte = bessere Qualität)
            '-c:a', 'aac',
            '-b:a', '128k',
            output_path
        ]
        
        try:
            # Starte ffmpeg und warte auf Abschluss
            subprocess.run(command, check=True)
            print(f"Konvertiert: {filename} -> {new_filename}")
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Konvertieren von {filename}: {e}")
