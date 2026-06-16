import winreg

ROOT = winreg.HKEY_CURRENT_USER
BASE = r"SOFTWARE\Classes"

EXTENSIONS = (
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
    ".mp4", ".avi", ".mov", ".wmv", ".flv",
    ".mp3", ".wav", ".aac", ".flac", ".ogg",
    ".txt", ".docx", ".pdf",
)

def delete_tree(hive, path):
    """Supprime récursivement une clé de registre et ses sous-clés."""
    try:
        with winreg.OpenKey(hive, path, access=winreg.KEY_ALL_ACCESS) as k:
            while True:
                try:
                    child = winreg.EnumKey(k, 0)
                    delete_tree(hive, rf"{path}\{child}")
                except OSError:
                    break
        winreg.DeleteKey(hive, path)
    except FileNotFoundError:
        pass 

def main():
    for ext in EXTENSIONS:
        key = rf"{BASE}\SystemFileAssociations\{ext}\shell\Convertir"
        delete_tree(ROOT, key)
        print(f"  {ext:8s} ✓")

    print("\nUninstall complete.")

if __name__ == "__main__":
    main()
