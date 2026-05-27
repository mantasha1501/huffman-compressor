from src.huffman_tree import build_tree, generate_codes

def compress(text):
    if not text:
        return "", None

    root = build_tree(text)
    huffman_codes = generate_codes(root)
    encoded_string = "".join(huffman_codes[char] for char in text)
    
    return encoded_string, root