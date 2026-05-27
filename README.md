# Huffman Coding File Compressor

A modular, lightweight command-line utility built in Python that compresses and decompresses text assets using optimal prefix codes derived from a Huffman Tree. 

This project demonstrates clean code structuring, file handling, and the practical application of greedy algorithms and binary tree data structures.

## How It Works

Instead of saving text where every character consumes a fixed 8 bits (1 byte), this engine assigns variable-length codes based on frequency:
1. **Frequency Maps:** Scans input text and calculates exact occurrence rates for individual characters.
2. **Min-Heap Construction:** Leverages a Priority Queue to continuously pair the lowest frequency nodes into a binary tree.
3. **Prefix Bit Generation:** Traces left child tracks (`0`) and right child tracks (`1`) starting from the root node to generate distinct paths for every unique character.

## Key Technical Implementations
* **Algorithmic Efficiency:** Uses custom node objects with standard library heaps for an efficient O(N log K) time complexity build phase.
* **Separation of Concerns:** Distinct decoupled files for structural generation, compression pathways, and decompression routines.
* **Defensive Design:** Gracefully catches file I/O faults and edge conditions (empty files) to eliminate standard software runtime crashes.

## Quick Start Instructions

Run the application entry file from your terminal:
```bash
python main.py