"""
Batch OCR Processor for Telugu Documents
Author: Lokesh Reddy

Features:
- Process multiple images in parallel
- Generate summary report
- Export to CSV/JSON formats
"""

import os
import json
import csv
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

from ocr_telugu import extract_with_confidence


def process_image(image_path: str) -> Dict:
    """Process single image and return results with metadata."""
    try:
        result = extract_with_confidence(image_path)
        return {
            'file': os.path.basename(image_path),
            'path': image_path,
            'status': 'success',
            'text': result['full_text'],
            'confidence': result['avg_confidence'],
            'word_count': len(result['words']),
            'low_confidence_words': [w for w in result['words'] if w['confidence'] < 80]
        }
    except Exception as e:
        return {
            'file': os.path.basename(image_path),
            'path': image_path,
            'status': 'failed',
            'error': str(e),
            'text': '',
            'confidence': 0,
            'word_count': 0
        }


def batch_process(input_folder: str, output_folder: str = None, 
                  max_workers: int = 4, export_format: str = 'txt') -> Dict:
    """
    Process all images in a folder with parallel execution.
    
    Args:
        input_folder: Folder containing images
        output_folder: Folder for output files (default: input_folder_output)
        max_workers: Number of parallel threads
        export_format: 'txt', 'json', or 'csv'
    
    Returns:
        Summary dictionary with processing results
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder) if output_folder else Path(f"{input_folder}_output")
    output_path.mkdir(exist_ok=True)
    
    # Find all images
    image_extensions = {'.png', '.jpg', '.jpeg', '.tiff', '.tif', '.bmp'}
    images = [f for f in input_path.iterdir() if f.suffix.lower() in image_extensions]
    
    if not images:
        print("No images found in folder!")
        return {'total': 0, 'success': 0, 'failed': 0}
    
    print(f"📷 Found {len(images)} images")
    print(f"🔄 Processing with {max_workers} threads...\n")
    
    results = []
    
    # Parallel processing
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_image, str(img)): img for img in images}
        
        for i, future in enumerate(as_completed(futures), 1):
            result = future.result()
            results.append(result)
            
            status = "✓" if result['status'] == 'success' else "✗"
            conf = f"{result['confidence']:.0f}%" if result['status'] == 'success' else "N/A"
            print(f"[{i}/{len(images)}] {status} {result['file']} (confidence: {conf})")
    
    # Save individual text files
    for result in results:
        if result['status'] == 'success':
            txt_file = output_path / f"{Path(result['file']).stem}.txt"
            txt_file.write_text(result['text'], encoding='utf-8')
    
    # Generate summary
    summary = {
        'timestamp': datetime.now().isoformat(),
        'input_folder': str(input_folder),
        'output_folder': str(output_path),
        'total': len(results),
        'success': sum(1 for r in results if r['status'] == 'success'),
        'failed': sum(1 for r in results if r['status'] == 'failed'),
        'avg_confidence': sum(r['confidence'] for r in results if r['status'] == 'success') / 
                          max(1, sum(1 for r in results if r['status'] == 'success')),
        'files': results
    }
    
    # Export summary
    if export_format == 'json':
        (output_path / 'summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    elif export_format == 'csv':
        with open(output_path / 'summary.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['file', 'status', 'confidence', 'word_count'])
            writer.writeheader()
            for r in results:
                writer.writerow({
                    'file': r['file'], 
                    'status': r['status'],
                    'confidence': r['confidence'],
                    'word_count': r['word_count']
                })
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"📊 BATCH PROCESSING COMPLETE")
    print(f"{'='*50}")
    print(f"   Total:      {summary['total']}")
    print(f"   Success:    {summary['success']}")
    print(f"   Failed:     {summary['failed']}")
    print(f"   Avg Conf:   {summary['avg_confidence']:.1f}%")
    print(f"   Output:     {output_path}")
    print(f"{'='*50}\n")
    
    return summary


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python batch_processor.py <input_folder> [output_folder]")
        print("\nExample:")
        print("  python batch_processor.py ./scanned_pages ./extracted_text")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None
    
    batch_process(input_folder, output_folder, export_format='json')
