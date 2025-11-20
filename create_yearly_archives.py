#!/usr/bin/env python3
import os
import re
import zipfile
from datetime import datetime
from pathlib import Path
from collections import defaultdict

EXTRACT_DIR = "takeout/temp_extract"
OUTPUT_DIR = "takeout/archives"
MAX_SIZE = 95 * 1024 * 1024  # 95MB to stay under 100MB

def extract_year_from_filename(filename):
    """Extract year from filename patterns like 20220517_130347.jpg or signal-2018-10-06-135914.jpg"""
    patterns = [
        r'(\d{4})\d{4}_\d{6}',  # 20220517_130347
        r'signal-(\d{4})-\d{2}-\d{2}',  # signal-2018-10-06
        r'(\d{4})-\d{2}-\d{2}',  # 2018-10-06
        r'^(\d{4})',  # starts with year
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            year = int(match.group(1))
            if 2000 <= year <= 2025:
                return year
    return None

def get_file_year(filepath):
    """Determine year from filename or modification time"""
    filename = os.path.basename(filepath)
    
    # Try filename first
    year = extract_year_from_filename(filename)
    if year:
        return year
    
    # Fall back to file modification time
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.fromtimestamp(mtime).year
    except:
        return None

def organize_files_by_year():
    """Organize all files by year"""
    files_by_year = defaultdict(list)
    
    for root, dirs, files in os.walk(EXTRACT_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            filesize = os.path.getsize(filepath)
            year = get_file_year(filepath)
            
            if year:
                files_by_year[year].append((filepath, filesize))
            else:
                files_by_year['unknown'].append((filepath, filesize))
    
    return files_by_year

def create_archives(files_by_year):
    """Create yearly archives under 100MB"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for year, files in sorted(files_by_year.items()):
        print(f"\nProcessing {year}: {len(files)} files")
        
        # Sort files by size (smallest first for better packing)
        files.sort(key=lambda x: x[1])
        
        part_num = 1
        current_zip = None
        current_size = 0
        
        for filepath, filesize in files:
            # Skip files larger than MAX_SIZE
            if filesize > MAX_SIZE:
                print(f"  Skipping large file: {os.path.basename(filepath)} ({filesize / 1024 / 1024:.1f}MB)")
                continue
            
            # Create new archive if needed
            if current_zip is None or current_size + filesize > MAX_SIZE:
                if current_zip:
                    current_zip.close()
                    print(f"  Created {archive_name} ({current_size / 1024 / 1024:.1f}MB)")
                
                archive_name = f"{year}_part{part_num:02d}.zip"
                archive_path = os.path.join(OUTPUT_DIR, archive_name)
                current_zip = zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED)
                current_size = 0
                part_num += 1
            
            # Add file to archive
            arcname = os.path.relpath(filepath, EXTRACT_DIR)
            current_zip.write(filepath, arcname)
            current_size += filesize
        
        if current_zip:
            current_zip.close()
            print(f"  Created {archive_name} ({current_size / 1024 / 1024:.1f}MB)")

def main():
    print("Organizing files by year...")
    files_by_year = organize_files_by_year()
    
    print("\nSummary:")
    for year in sorted(files_by_year.keys()):
        total_size = sum(f[1] for f in files_by_year[year]) / 1024 / 1024
        print(f"  {year}: {len(files_by_year[year])} files, {total_size:.1f}MB")
    
    print("\nCreating archives...")
    create_archives(files_by_year)
    
    print("\nDone!")

if __name__ == "__main__":
    main()
