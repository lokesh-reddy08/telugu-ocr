#!/usr/bin/env python3
"""
Telugu OCR Command Line Interface
Author: Lokesh Reddy

Usage:
    python cli.py image.png                    # Extract text from single image
    python cli.py image.png -o output.txt      # Save to file
    python cli.py folder/ --batch              # Process all images in folder
    python cli.py image.png --lang tel+eng     # Mixed language mode
"""

import argparse
import os
import sys
from pathlib import Path

from ocr_telugu import extract_telugu_text, extract_with_confidence, preprocess_image


def process_single_image(image_path: str, lang: str = 'tel', preprocess: bool = False, 
                         show_confidence: bool = False) -> str:
    """Process a single image and return extracted text."""
    import pytesseract
    from PIL import Image
    
    if preprocess:
        img = preprocess_image(image_path)
    else:
        img = Image.open(image_path)
    
    if show_confidence:
        result = extract_with_confidence(image_path)
        output = f"Text:\n{result['full_text']}\n"
        output += f"\nAverage Confidence: {result['avg_confidence']:.1f}%\n"
        
        low_conf = [w for w in result['words'] if w['confidence'] < 80]
        if low_conf:
            output += "\n⚠️ Low confidence words:\n"
            for w in low_conf:
                output += f"  - '{w['word']}' ({w['confidence']}%)\n"
        return output
    else:
        return pytesseract.image_to_string(img, lang=lang)


def process_batch(folder_path: str, output_folder: str, lang: str = 'tel', 
                  preprocess: bool = False) -> dict:
    """Process all images in a folder."""
    results = {'success': 0, 'failed': 0, 'files': []}
    
    image_extensions = {'.png', '.jpg', '.jpeg', '.tiff', '.tif', '.bmp', '.gif'}
    folder = Path(folder_path)
    output_dir = Path(output_folder)
    output_dir.mkdir(exist_ok=True)
    
    for img_file in folder.iterdir():
        if img_file.suffix.lower() in image_extensions:
            try:
                print(f"Processing: {img_file.name}...", end=" ")
                text = process_single_image(str(img_file), lang, preprocess)
                
                # Save output
                out_file = output_dir / f"{img_file.stem}.txt"
                out_file.write_text(text, encoding='utf-8')
                
                results['success'] += 1
                results['files'].append(str(img_file.name))
                print("✓")
            except Exception as e:
                results['failed'] += 1
                print(f"✗ ({e})")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Telugu OCR Tool - Extract Telugu text from images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py document.png                     Extract text and print to console
  python cli.py document.png -o result.txt       Save extracted text to file
  python cli.py ./scans/ --batch -o ./texts/     Process all images in folder
  python cli.py document.png --confidence        Show confidence scores
  python cli.py document.png --preprocess        Apply image enhancement first
  python cli.py document.png --lang tel+eng      For mixed Telugu-English text

Author: Lokesh Reddy
        """
    )
    
    parser.add_argument('input', help='Image file or folder path')
    parser.add_argument('-o', '--output', help='Output file or folder path')
    parser.add_argument('--batch', action='store_true', help='Process all images in folder')
    parser.add_argument('--lang', default='tel', help='Language code (default: tel)')
    parser.add_argument('--preprocess', action='store_true', help='Apply image preprocessing')
    parser.add_argument('--confidence', action='store_true', help='Show confidence scores')
    parser.add_argument('--version', action='version', version='Telugu OCR v1.0.0')
    
    args = parser.parse_args()
    
    # Validate input
    if not os.path.exists(args.input):
        print(f"Error: '{args.input}' not found")
        sys.exit(1)
    
    # Batch processing
    if args.batch:
        if not os.path.isdir(args.input):
            print("Error: --batch requires a folder path")
            sys.exit(1)
        
        output_folder = args.output or f"{args.input}_ocr_output"
        print(f"\n📁 Batch OCR Processing")
        print(f"   Input:  {args.input}")
        print(f"   Output: {output_folder}\n")
        
        results = process_batch(args.input, output_folder, args.lang, args.preprocess)
        
        print(f"\n✅ Complete: {results['success']} processed, {results['failed']} failed")
        return
    
    # Single file processing
    print(f"\n🔍 Extracting text from: {args.input}")
    print(f"   Language: {args.lang}\n")
    
    try:
        text = process_single_image(args.input, args.lang, args.preprocess, args.confidence)
        
        if args.output:
            Path(args.output).write_text(text, encoding='utf-8')
            print(f"✅ Saved to: {args.output}")
        else:
            print("-" * 50)
            print(text)
            print("-" * 50)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
