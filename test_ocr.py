"""
Test script to verify OCR setup works correctly.
Run: python test_ocr.py
"""

import os
import sys
from PIL import Image, ImageDraw

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ocr_telugu import extract_telugu_text, extract_with_confidence, preprocess_image


def create_test_image():
    """Create a simple test image with English text."""
    img = Image.new('RGB', (400, 100), color='white')
    draw = ImageDraw.Draw(img)
    draw.text((20, 30), "Hello World OCR Test 123", fill='black')
    test_path = "test_image.png"
    img.save(test_path)
    return test_path


def run_tests():
    print("=" * 50)
    print("Telugu OCR - Test Suite")
    print("=" * 50)
    
    # Test 1: Basic extraction
    print("\n[Test 1] Basic text extraction...")
    test_img = create_test_image()
    
    try:
        # Test with English first (more reliable)
        import pytesseract
        text = pytesseract.image_to_string(Image.open(test_img), lang='eng')
        if "Hello" in text or "World" in text or "OCR" in text:
            print("✓ Basic OCR working!")
        else:
            print(f"△ OCR returned: {text.strip()}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 2: Telugu language support
    print("\n[Test 2] Telugu language check...")
    try:
        import pytesseract
        langs = pytesseract.get_languages()
        if 'tel' in langs:
            print("✓ Telugu language pack installed!")
        else:
            print("✗ Telugu NOT found. Install tel.traineddata")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 3: Confidence extraction
    print("\n[Test 3] Confidence scoring...")
    try:
        result = extract_with_confidence(test_img)
        print(f"✓ Avg confidence: {result['avg_confidence']:.1f}%")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 4: Preprocessing
    print("\n[Test 4] Image preprocessing...")
    try:
        processed = preprocess_image(test_img)
        print(f"✓ Preprocessed image: {processed.size}")
    except Exception as e:
        print(f"△ Preprocessing: {e}")
    
    # Cleanup
    if os.path.exists(test_img):
        os.remove(test_img)
    
    print("\n" + "=" * 50)
    print("Tests complete!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
