# File Converter

Adds a **"Convert to..."** submenu to the Windows Explorer right-click menu.

## Supported formats

| Type | Formats |
|------|---------|
| Images | JPEG, PNG, GIF, BMP, TIFF, WebP |
| Video | MP4, AVI, MOV, WMV, FLV | and audio extraction with MP4 to MP3
| Audio | MP3, WAV, AAC, FLAC, OGG |
| Documents | PDF, DOCX, TXT |

## Requirements

- Windows 10/11
- Python 3.8+
- Microsoft Word (optional, for DOCX → PDF only)

## Installation

```
setup.bat
```

That's it. The context menu is registered automatically.  
ffmpeg is downloaded automatically on first use (~80 MB).

## Usage

Right-click any supported file → **Show more options** → **Convert to...** → pick a format.

The converted file is saved in the same folder as the source file.

## Uninstall

```
python uninstall.py
```

Removes the context menu entries from the registry. Does not delete ffmpeg or any converted files.

## Project structure

```
fileConverter/
├── converter.py    # conversion logic
├── install.py      # registers the context menu
├── uninstall.py    # removes the context menu
├── setup.bat       # one-click install
└── ffmpeg/         # ffmpeg.exe (auto-downloaded)
```
