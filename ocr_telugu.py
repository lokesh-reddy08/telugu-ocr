"""
Telugu OCR Script using Tesseract
For OKI-IIIT Hyderabad Internship Preparation

Author: P. Lokesh Reddy
Date: April 2026

SETUP:
1. Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
   - Select Telugu language during installation
2. pip install pytesseract pillow opencv-python
"""

import pytesseract
from PIL import Image
import os
import sys

# Configure Tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_telugu_text(image_path: str) -> str:
    """
    Extract Telugu text from an image using Tesseract OCR.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Extracted Telugu text as string
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    image = Image.open(image_path)
    
    # 'tel' = Telugu, 'tel+eng' for mixed text
    text = pytesseract.image_to_string(image, lang='tel')
    return text


def extract_with_confidence(image_path: str) -> dict:
    """
    Extract text with confidence scores for each word.
    Useful for identifying potential OCR errors.
    """
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, lang='tel', output_type=pytesseract.Output.DICT)
    
    results = []
    for i, word in enumerate(data['text']):
        if word.strip():
            results.append({
                'word': word,
                'confidence': data['conf'][i],
            })
    
    avg_conf = sum(r['confidence'] for r in results) / len(results) if results else 0
    
    return {
        'words': results,
        'full_text': pytesseract.image_to_string(image, lang='tel'),
        'avg_confidence': avg_conf
    }


def preprocess_image(image_path: str):
    """
    Preprocess image for better OCR accuracy.
    Uses grayscale conversion and thresholding.
    """
    try:
        import cv2
        import numpy as np
        
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        return Image.fromarray(binary)
    except ImportError:
        print("OpenCV not installed. Using original image.")
        return Image.open(image_path)


def main():
    """Main function with usage examples."""
    
    print("=" * 50)
    print("Telugu OCR Tool - OKI Internship Preparation")
    print("=" * 50)
    
    # Check Tesseract installation
    try:
        version = pytesseract.get_tesseract_version()
        print(f"✓ Tesseract version: {version}")
    except Exception as e:
        print(f"✗ Tesseract not found!")
        print("\nInstall from: https://github.com/UB-Mannheim/tesseract/wiki")
        print("Select 'Telugu' language during installation")
        sys.exit(1)
    
    # Check Telugu support
    try:
        languages = pytesseract.get_languages()
        if 'tel' in languages:
            print("✓ Telugu language pack installed")
        else:
            print("✗ Telugu NOT found. Reinstall with Telugu support.")
    except:
        pass
    
    print("\n" + "=" * 50)
    print("USAGE EXAMPLES:")
    print("=" * 50)
    print("""
# Basic OCR
from ocr_telugu import extract_telugu_text
text = extract_telugu_text('your_image.png')
print(text)

# With confidence scores
from ocr_telugu import extract_with_confidence
result = extract_with_confidence('your_image.png')
print(f"Confidence: {result['avg_confidence']:.1f}%")

# Find low-confidence words (likely errors)
for word in result['words']:
    if word['confidence'] < 80:
        print(f"Check: {word['word']} ({word['confidence']}%)")
""")
    
    # Demo with sample if exists
    sample = 'sample_telugu.png'
    if os.path.exists(sample):
        print("\nRunning OCR on sample...")
        text = extract_telugu_text(sample)
        print(f"\nExtracted:\n{text}")
    else:
        print(f"\nCreate '{sample}' to test OCR")


if __name__ == "__main__":
    main()
