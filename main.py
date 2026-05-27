import os
from src.encoder import compress
from src.decoder import decompress

def run_tool():
    print("=========================================")
    print("   Huffman Coding File Compressor CLI   ")
    print("=========================================\n")
    
    filename = "sample.txt"
    
    if not os.path.exists(filename):
        print(f"[Error] '{filename}' was not found.")
        print("Please create a 'sample.txt' file in the root directory first.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        original_text = file.read()

    if not original_text.strip():
        print("[Warning] The sample.txt file is empty. Nothing to compress.")
        return

    print(f"Reading '{filename}' successful ({len(original_text)} characters)...")
    
    encoded_bits, tree_root = compress(original_text)
    
    original_size_bits = len(original_text) * 8
    compressed_size_bits = len(encoded_bits)
    savings = 100 - (compressed_size_bits / original_size_bits * 100)

    print("\n--- Compression Metrics ---")
    print(f"Original Size:   {original_size_bits} bits")
    print(f"Compressed Size: {compressed_size_bits} bits")
    print(f"Space Reduction: {savings:.2f}%")
    
    decompressed_text = decompress(encoded_bits, tree_root)
    
    print("\n--- Integrity Verification ---")
    if original_text == decompressed_text:
        print("Success! Decompressed text matches original text perfectly.")
    else:
        print("Mismatch detected during reconstruction process.")

if __name__ == "__main__":
    run_tool()