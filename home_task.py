import os
import shutil
import re

from transliterate import translit

def normalize(filename):
    normalized_name = translit(filename, 'ru', reversed=True)
    normalized_name = re.sub(r'[^a-zA-Z0-9_.]', '_', normalized_name)
    return normalized_name

def sort_files(folder_path):
    # Список відомих розширень для кожної категорії
    known_extensions = {
        'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
        'video': ('AVI', 'MP4', 'MOV', 'MKV'),
        'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
        'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
        'archives': ('ZIP', 'GZ', 'TAR'),
    }

    for category in known_extensions:
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

    unknown_extensions = set()  # не відомо що це за файли

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            extension = filename.split('.')[-1].upper()

            # Перевірка, чи відоме розширення
            moved = False
            for category, extensions in known_extensions.items():
                if extension in extensions:
                    # Перейменування та переміщення файлу до відповідної папки
                    new_name = normalize(filename)
                    new_path = os.path.join(folder_path, category, new_name)
                    shutil.move(file_path, new_path)
                    moved = True
                    break

            if not moved:
                # Файл невідомі
                unknown_extensions.add(extension)

    # Видалення порожніх папок
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

    return known_extensions, list(unknown_extensions)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python homo_task.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        known_extensions, unknown_extensions = sort_files(folder_path)

        print("Known Extensions:")
        for category, ext_list in known_extensions.items():
            print(f"{category}: {', '.join(ext_list)}")

        print("\nUnknown Extensions:")
        print(', '.join(unknown_extensions))
