"""
install.py — registers the "Convert to..." context menu in the Windows registry
No admin rights required (writes to HKCU).
"""
import sys
import os
import winreg
from pathlib import Path

PYTHON = sys.executable
SCRIPT = str(Path(__file__).parent / "converter.py")
ROOT   = winreg.HKEY_CURRENT_USER
BASE   = r"SOFTWARE\Classes"

# Mapping extension → options de conversion
MENUS = {
    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif"): [
        ("JPEG",              "jpg"),
        ("PNG",               "png"),
        ("GIF",               "gif"),
        ("BMP",               "bmp"),
        ("TIFF",              "tiff"),
        ("WebP",              "webp"),
    ],
    (".mp4", ".avi", ".mov", ".wmv", ".flv"): [
        ("MP4",               "mp4"),
        ("AVI",               "avi"),
        ("MOV",               "mov"),
        ("WMV",               "wmv"),
        ("FLV",               "flv"),
        ("MP3 (audio only)",  "mp3"),
    ],
    (".mp3", ".wav", ".aac", ".flac", ".ogg"): [
        ("MP3",               "mp3"),
        ("WAV",               "wav"),
        ("AAC",               "aac"),
        ("FLAC",              "flac"),
        ("OGG",               "ogg"),
    ],
    (".txt",):  [("PDF", "pdf"), ("DOCX", "docx")],
    (".docx",): [("PDF", "pdf"), ("TXT",  "txt")],
    (".pdf",):  [("TXT", "txt")],
}

def set_val(key, name, value):
    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)

def register_ext(ext: str, formats: list):
    shell_key = rf"{BASE}\SystemFileAssociations\{ext}\shell\Convertir"

    with winreg.CreateKey(ROOT, shell_key) as k:
        set_val(k, "MUIVerb",     "Convertir en...")
        set_val(k, "SubCommands", "")           

    for label, fmt in formats:
        with winreg.CreateKey(ROOT, rf"{shell_key}\shell\{fmt}") as k:
            set_val(k, "", label)
        with winreg.CreateKey(ROOT, rf"{shell_key}\shell\{fmt}\command") as k:
            set_val(k, "", f'"{PYTHON}" "{SCRIPT}" "%1" {fmt}')

def main():
    print(f"Python : {PYTHON}")
    print(f"Script : {SCRIPT}")
    print()

    for exts, formats in MENUS.items():
        for ext in exts:
            register_ext(ext, formats)
            labels = ", ".join(f for _, f in formats)
            print(f"  {ext:8s} → {labels}")

    print("\nInstallation complete.")
    print("If the menu does not appear, restart Windows Explorer:")
    print("Task Manager → Windows Explorer → Restart.")

if __name__ == "__main__":
    main()
