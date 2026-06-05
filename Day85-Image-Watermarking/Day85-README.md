# Day 85 – Chill Watermarking App 🖼️

A desktop application with a Graphical User Interface (GUI) that automatically adds a text watermark to images to
protect digital copyrights.

## Features

- **Image Upload:** Supports various image formats (.png, .jpg, .jpeg, .bmp, .webp).
- **Auto-Resize Preview:** Automatically scales down high-resolution images to fit smoothly inside a 400x400 canvas
  preview.
- **Smart UI Workflow:** Dynamic button states that guide users through a clean step-by-step process (Upload → Add
  Watermark → Save).
- **Transparent Overlay:** Blends a customizable text layer seamlessly onto the base image with a perfect opacity
  balance.

## Tech Stack

- Python 3
- **CustomTkinter:** Modern and clean GUI components.
- **Pillow (PIL):** Advanced image processing, blending (Alpha Composite), and resizing.

## How to Run

```bash
pip install customtkinter Pillow
python main.py
```