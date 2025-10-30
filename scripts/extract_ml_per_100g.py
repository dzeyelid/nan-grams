#!/usr/bin/env python3
"""
Extract food items with ml per 100g information from Japanese Food Standard Composition Table CSV.

This script reads the CSV file containing data from "日本食品標準成分表（八訂）増補2023年" 
for "17 調味料及び香辛料類" (Seasonings and Spices) and extracts items that have 
ml per 100g information in the remarks column.

Output: JSON file with list of food names and their ml per 100g values.
"""

import csv
import json
import re
from pathlib import Path


def extract_ml_per_100g(csv_path, output_path):
    """
    Extract items with ml per 100g from the CSV file.
    
    Args:
        csv_path: Path to the input CSV file
        output_path: Path to the output JSON file
    
    Returns:
        List of dictionaries containing food_name and ml_per_100g
    """
    results = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
        # Column indices based on CSV structure:
        # - Column 3: 食品名 (Food name)
        # - Column 61: 備考 (Remarks)
        FOOD_NAME_COL = 3
        REMARKS_COL = 61
        
        # Start from row 4 (skip header rows and metadata rows)
        for i in range(4, len(rows)):
            if len(rows[i]) > REMARKS_COL:
                food_name = rows[i][FOOD_NAME_COL].strip()
                remarks = rows[i][REMARKS_COL].strip()
                
                if food_name and remarks:
                    # Look for pattern like "100 g： XX.X mL" or "100 g: XX.X ml"
                    match = re.search(r'100\s*g[：:]\s*([\d.]+)\s*m[Ll]', remarks)
                    if match:
                        ml_per_100g = match.group(1)
                        results.append({
                            'food_name': food_name,
                            'ml_per_100g': float(ml_per_100g)
                        })
    
    # Save to JSON file
    output_data = {
        'source': '日本食品標準成分表（八訂）増補2023年 - 17 調味料及び香辛料類',
        'description': '備考欄に100gあたりのmlが記載されている項目',
        'count': len(results),
        'items': results
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"Extracted {len(results)} items with ml per 100g")
    print(f"Output saved to: {output_path}")
    
    return results


def main():
    # Define paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    csv_path = repo_root / 'references' / '20230428-mxt_kagsei-mext_00001_012(17調味料及び香辛料類).csv'
    output_path = repo_root / 'data' / 'ml_per_100g.json'
    
    # Create data directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Extract and save data
    results = extract_ml_per_100g(csv_path, output_path)
    
    # Print sample results
    print("\nSample results:")
    for item in results[:5]:
        print(f"  - {item['food_name']}: {item['ml_per_100g']} ml")
    print(f"  ... and {len(results) - 5} more items")


if __name__ == '__main__':
    main()
