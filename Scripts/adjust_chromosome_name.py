#!/usr/bin/env python3
"""
Script to replace specific chromosome names in a SAM file.

This script reads an input SAM file, removes suffixes, and writes
the modified content to a new output SAM file.

"""

# Dictionary mapping old accession numbers to new ones
replacements = {
    "LT962476.2": "LT962476",
    "LT962477.2": "LT962477",
    "LT962478.2": "LT962478",
    "LT962479.2": "LT962479",
    "FR839632.1": "FR839632"
}

def process_sam_file(input_path, output_path):
    """
    Reads a SAM file, replaces specified accession numbers, and writes the result to a new file.

    Parameters:
        input_path (str): Path to the input SAM file.
        output_path (str): Path to the output SAM file.
    """
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            for old, new in replacements.items():
                line = line.replace(old, new)
            outfile.write(line)

# Example usage
if __name__ == "__main__":
    input_file = "reference.sam"   # Replace with your actual input file name
    output_file = "reference_cleaned.sam" # Replace with your desired output file name
    process_sam_file(input_file, output_file)
    print(f"Processing complete. Modified file saved as '{output_file}'.")