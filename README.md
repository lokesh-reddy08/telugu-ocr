# Telugu OCR Tool 📜

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tesseract](https://img.shields.io/badge/Tesseract-5.0+-green.svg)](https://github.com/tesseract-ocr/tesseract)

A Python-based OCR (Optical Character Recognition) tool for extracting Telugu text from images. Built using Tesseract OCR with support for confidence scoring, image preprocessing, and batch processing.

## ✨ Features

- **Telugu Text Extraction** - Extract Telugu text from scanned documents, book pages, screenshots
- **Confidence Scoring** - Get word-level confidence scores to identify potential OCR errors
- **Image Preprocessing** - Grayscale conversion and Otsu thresholding for improved accuracy
- **Mixed Language Support** - Works with Telugu + English mixed content
- **Command Line Interface** - Easy-to-use CLI for quick processing
- **Batch Processing** - Process entire folders with parallel execution
- **Multiple Export Formats** - Export results as TXT, JSON, or CSV

## 🚀 Installation

### Prerequisites

1. **Install Tesseract OCR** (Windows)
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - During installation, select **Telugu** language pack
   - Or download `tel.traineddata` from [tessdata_best](https://github.com/tesseract-ocr/tessdata_best) and place in `C:\Program Files\Tesseract-OCR\tessdata\`

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Verify Installation
```bash
python test_ocr.py
```

## 📖 Usage

### Basic Text Extraction
```python
from ocr_telugu import extract_telugu_text

text = extract_telugu_text('telugu_document.png')
print(text)
```

### With Confidence Scores
```python
from ocr_telugu import extract_with_confidence

result = extract_with_confidence('telugu_document.png')
print(f"Average Confidence: {result['avg_confidence']:.1f}%")

# Find words that may have OCR errors
for word in result['words']:
    if word['confidence'] < 80:
        print(f"⚠️ Check: {word['word']} ({word['confidence']}%)")
```

### Image Preprocessing
```python
from ocr_telugu import preprocess_image
from PIL import Image
import pytesseract

# Preprocess for better accuracy
processed_img = preprocess_image('low_quality_scan.png')
text = pytesseract.image_to_string(processed_img, lang='tel')
```

## 💻 Command Line Interface

```bash
# Basic usage
python cli.py document.png

# Save output to file
python cli.py document.png -o result.txt

# Process with confidence scores
python cli.py document.png --confidence

# Apply image preprocessing
python cli.py document.png --preprocess

# Mixed Telugu-English text
python cli.py document.png --lang tel+eng

# Batch process entire folder
python cli.py ./scans/ --batch -o ./output/
```

## 📦 Batch Processing

Process multiple images with parallel execution:

```bash
python batch_processor.py ./scanned_pages ./extracted_text
```

Features:
- Multi-threaded processing (4 threads default)
- Generates summary report (JSON/CSV)
- Tracks confidence scores for quality control

## 📁 Project Structure

```
telugu-ocr/
├── ocr_telugu.py        # Core OCR module
├── cli.py               # Command line interface
├── batch_processor.py   # Batch processing with parallelization
├── test_ocr.py          # Test suite
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
├── README.md            # Documentation
└── .gitignore
```

## 🔧 Configuration

If Tesseract is installed in a non-default location, update the path in `ocr_telugu.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Your\Path\tesseract.exe'
```

## 🤝 Contributing to Telugu Wikisource

This project was created as preparation for contributing to Telugu digital preservation. You can help digitize Telugu literature at:

- **Telugu Wikisource**: https://te.wikisource.org
- Proofread OCR'd pages and correct errors
- Help preserve Telugu literary heritage

## 📝 License

MIT License - Feel free to use and modify!

## 👤 Author

**Lokesh Reddy**

- 📧 plokeshreddy5678@gmail.com
- 🎓 B.Tech CSE (Cyber Security) - Geethanjali College of Engineering
- 📊 BS Data Science - IIT Madras
- 🔗 GitHub: [@lokeshreddy](https://github.com/lokeshreddy)

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Open source OCR engine
- [Telugu Wikisource](https://te.wikisource.org) - Telugu digital library


---


