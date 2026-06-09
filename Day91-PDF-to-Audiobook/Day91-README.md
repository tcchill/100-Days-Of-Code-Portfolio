# Day 91 – PDF to Audiobook 🎧

A Python tool that automatically converts PDF documents into MP3 audiobooks using Google Cloud Text-to-Speech API.

## Features

- Extract text from multi-page PDF files
- Convert extracted text to natural-sounding speech
- Output high-quality MP3 audio file
- Supports Vietnamese voice (vi-VN-Neural2-D)

## Tech Stack

- Python 3
- `pypdf` — PDF text extraction
- `google-cloud-texttospeech` — Text-to-Speech conversion

## Setup

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Set up Google Cloud credentials**

- Create a project on [Google Cloud Console](https://console.cloud.google.com/)
- Enable the **Text-to-Speech API**
- Download your service account key as a `.json` file
- Set the environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key.json"
```

## How to Run

```bash
python main.py
```

Output audio will be saved as `output.mp3` in the same directory.

## What I Learned

- Extracting and processing text from PDF files with `pypdf`
- Integrating Google Cloud Text-to-Speech API
- Handling multi-page PDF documents
- Working with binary file output (MP3)