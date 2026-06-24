# File Converter — Convert files from the Windows right-click menu

**Convert images, videos, audio and documents directly from the Windows Explorer right-click menu — no app to open, no website to upload your files to.**

File Converter adds a **"Convert to..."** submenu to the Windows context menu. Right-click any file, pick a target format, and the converted file appears in the same folder. It works fully offline on your own PC, so your files are never uploaded to an online converter.

If you have ever searched for *"how to convert a file in Windows without software"*, *"free file converter no upload"*, *"convert WebP to PNG Windows"*, *"convert MP4 to MP3 right-click"*, or *"batch image converter Windows Explorer"* — this is what this tool does.

## Why use it?

Most file conversion means either installing bloated software or uploading private files to a sketchy online converter. File Converter solves both problems:

- **No upload, fully offline** — your files stay on your machine (privacy-friendly).
- **No app to launch** — convert straight from the right-click menu.
- **Free and open source** — powered by Python, Pillow and ffmpeg.
- **One-click install** — a single `setup.bat` registers everything.

## Features

- Convert directly from the **Windows Explorer right-click / context menu**
- **Image conversion**: JPEG, PNG, GIF, BMP, TIFF, WebP, SVG
- **Video conversion**: MP4, AVI, MOV, WMV, FLV
- **Extract audio from video** (e.g. **MP4 → MP3**)
- **Audio conversion**: MP3, WAV, AAC, FLAC, OGG
- **Document conversion**: PDF, DOCX, TXT
- **Image to SVG** vectorization (monochrome silhouette you can recolor)
- **SVG to image** rasterization to any format
- Converted file saved next to the original — no clutter

## Supported formats

| Type | Convert between |
|------|---------|
| Images | JPEG, PNG, GIF, BMP, TIFF, WebP, SVG |
| Video | MP4, AVI, MOV, WMV, FLV (+ audio extraction, e.g. MP4 → MP3) |
| Audio | MP3, WAV, AAC, FLAC, OGG |
| Documents | PDF, DOCX, TXT |

Converting an image **to SVG** vectorizes it as a monochrome silhouette (single
`fill`), so the result can be recolored afterwards. Converting **from SVG**
rasterizes it to any image format.

## Requirements

- Windows 10 / 11
- Python 3.8+
- Microsoft Word (optional, only for DOCX → PDF)

## Installation

```
setup.bat
```

That's it. The **"Convert to..."** context menu is registered automatically.
ffmpeg is downloaded automatically on first use (~80 MB) for video and audio conversion.

## Usage

1. **Right-click** any supported file in Windows Explorer.
2. Click **Show more options** (on Windows 11) to reveal the full menu.
3. Open the **Convert to...** submenu.
4. Pick the target format.

The converted file is saved in the **same folder** as the source file.

### Examples

- Convert a **WebP image to PNG**: right-click the `.webp` file → Convert to... → PNG
- Extract **MP3 audio from an MP4 video**: right-click the `.mp4` file → Convert to... → MP3
- Convert a **PNG logo to SVG**: right-click the `.png` file → Convert to... → SVG
- Convert a **DOCX to PDF**: right-click the `.docx` file → Convert to... → PDF

## Uninstall

```
uninstall.bat
```

Removes the **"Convert to..."** context menu entries from the registry. Does not delete ffmpeg or any converted files.

## Project structure

```
File-converter/
├── setup.bat           # one-click install (deps + context menu)
├── uninstall.bat       # removes the context menu
├── ffmpeg/             # ffmpeg.exe (auto-downloaded on first use)
└── src/
    ├── converter.py    # conversion logic
    ├── install.py      # registers the context menu
    └── uninstall.py    # removes the context menu
```

## Keywords

Windows file converter, right-click file converter, context menu converter, convert files without software, offline file converter, free file converter no upload, image converter Windows, WebP to PNG, MP4 to MP3, video to audio, PDF converter, DOCX to PDF, SVG converter, Explorer right-click convert.
