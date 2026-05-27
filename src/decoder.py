def decompress(encoded_string, root):
    if not encoded_string or root is None:
        return ""

    decoded_output = []
    current_node = root

    for bit in encoded_string:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_output.append(current_node.char)
            current_node = root

    return "".join(decoded_output)