#!/bin/bash

# Check that two arguments were provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 filename width" >&2
  exit 1
fi

# Extract the arguments
filename="$1"
width="$2"

# Check that the file exists
if [ ! -f "$filename" ]; then
  echo "File not found: $filename" >&2
  exit 1
fi

# Get the original image dimensions
original_width=$(identify -format "%w" "$filename")
original_height=$(identify -format "%h" "$filename")

# Calculate the new height while maintaining aspect ratio
height=$(echo "scale=0;$original_height*($width/$original_width)" | bc -l)

# Resize and convert to WebP
echo cwebp -q 100 --preset photo -resize  "$width" "$height" "$filename" -o "${filename%.*}_resized.webp"
cwebp -resize "$width" "$height" "$filename" -o "${filename%.*}_resized.webp"
