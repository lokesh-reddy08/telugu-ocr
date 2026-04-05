# Telugu OCR Tool 📜

A Python-based OCR (Optical Character Recognition) tool for extracting Telugu text from images. Built using Tesseract OCR with support for confidence scoring and image preprocessing.

## ✨ Features

- **Telugu Text Extraction** - Extract Telugu text from scanned documents, book pages, screenshots
- **Confidence Scoring** - Get word-level confidence scores to identify potential OCR errors
- **Image Preprocessing** - Grayscale conversion and Otsu thresholding for improved accuracy
- **Mixed Language Support** - Works with Telugu + English mixed content

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

## 📁 Project Structure

```
telugu-ocr-project/
├── ocr_telugu.py      # Main OCR module
├── test_ocr.py        # Test suite
├── requirements.txt   # Python dependencies
├── README.md          # This file
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

**P. Lokesh Reddy**
- B.Tech CSE (Cyber Security) - Geethanjali College of Engineering
- BS Data Science - IIT Madras

---

*Built for OKI-IIIT Hyderabad Digital Preservation Initiative*
