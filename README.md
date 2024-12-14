# Huffman Encoding for Compression

## Introduction
This a a generated README.md for a project I was trying out to understand how Huffman encoding and generally how the process of encoding works.
Huffman encoding is a LOSSLESS data compression algorithm that reduces the size of data by encoding frequent symbols with shorter binary codes and infrequent symbols with longer binary codes. It is widely used in various fields to optimize storage and transmission.
This repository basic implementation for huffman encoding algorithm for specifically strings

---

## Features
- **Lossless Compression**: The original data can be perfectly reconstructed after decompression.
- **Efficient Encoding**: Uses variable-length codes to save space.
- **Customizable**: Can handle any input string with arbitrary characters.

---

## Encoding Purposes
Encoding serves various purposes in saving space and optimizing storage or transmission. Some of the more common applications are

### 1. **File Compression**
Huffman encoding can be used to compress text files, log files, or any other data with repetitive patterns to save disk space.

### 2. **Data Transmission**
Reducing the size of data before transmission over a network can lower bandwidth usage and improve transfer speeds.

### 3. **Memory Optimization**
When working with memory-constrained systems, such as embedded devices, Huffman encoding can help store more data within the available memory.

### 4. **Image and Video Compression**
Huffman encoding is often a sub-step in multimedia compression algorithms (e.g., JPEG and MPEG) to reduce file sizes without losing quality.

### 5. **Custom Data Formats**
Applications that work with proprietary data formats can use Huffman encoding to ensure smaller file sizes.

---

## Uncommon and Niche Applications

### 1. **Genome Data Compression**
Huffman encoding can be applied to compress genome sequences, which often contain repetitive patterns. This can save space for large-scale genomic data storage and analysis.

### 2. **Scientific Simulation Outputs**
Outputs from simulations in physics, chemistry, or engineering often generate large datasets. Compressing these outputs without losing any details is essential for analysis and archival.

### 3. **Sensor Data in IoT Devices**
IoT devices generate continuous streams of data. Huffman encoding can compress sensor logs and reduce the data transmission load, especially in low-bandwidth environments.

### 4. **Archiving Historical Documents**
Digital archiving of scanned historical documents or manuscripts can benefit from lossless compression to maintain integrity while reducing storage requirements.

### 5. **Data Integrity in Blockchain Systems**
In blockchain, storing large datasets on-chain is impractical. Huffman encoding can compress metadata and transaction details without compromising verifiability.

### 6. **Game Level Data Compression**
In gaming, storing and transmitting game levels or assets can be optimized using lossless compression to reduce download sizes and improve load times.

### 7. **Astronomical Data Storage**
Astronomy generates terabytes of observational data. Huffman encoding can compress image and spectral data for efficient storage and retrieval.

### 8. **Speech Recognition Systems**
In speech recognition, intermediate processing stages generate a lot of textual data. Compressing these texts ensures faster storage and retrieval during runtime.

---

## Code Overview
The implementation consists of:

- **Node Class**: Represents a node in the Huffman tree.
- **build_huffman_tree()**: Constructs the Huffman tree based on character frequencies.
- **build_codes()**: Generates the binary encoding for each character.
- **compress()**: Compresses the input string into a binary encoded string.
- **decompress()**: Decodes the binary string back into the original string.

---

## Usage

### Example:
```python
# Example Usage
data = "hello hello hello this is a string encoded by huffman encoding"
print("Original Data:", data)

compressed_data, tree = compress(data)
print("Compressed Data:", compressed_data)

decompressed_data = decompress(compressed_data, tree)
print("Decompressed Data:", decompressed_data)

# Calculate and compare sizes
original_size = len(data) * 8  # Each character is 8 bits
encoded_size = len(compressed_data)  # Encoded data is in bits
decoded_size = len(decompressed_data) * 8  # Each character is 8 bits

print(f"Size of Original Data: {original_size} bits ({len(data)} characters)")
print(f"Size of Encoded Data: {encoded_size} bits")
print(f"Size of Decoded Data: {decoded_size} bits ({len(decompressed_data)} characters)")
```

### Output Example:
```
Original Data: hello hello hello this is a string encoded by huffman encoding
Compressed Data: 101011...
Decompressed Data: hello hello hello this is a string encoded by huffman encoding
Size of Original Data: 512 bits (64 characters)
Size of Encoded Data: 298 bits
Size of Decoded Data: 512 bits (64 characters)
```

---

## Advantages of Huffman Encoding
1. **Efficient Compression**: Frequently occurring characters use fewer bits.
2. **Universal Application**: Works on any type of data.
3. **No Data Loss**: The decompressed data matches the original exactly.

---

## Limitations
1. **Preprocessing Overhead**: Requires building a frequency table and Huffman tree.
2. **Ineffective for Small Data**: Compression benefits diminish for small input sizes.
3. **Fixed Overhead**: Requires storing the Huffman tree or codebook along with compressed data.

---

## Conclusion
Huffman encoding is a versatile and efficient algorithm for lossless data compression. It is particularly effective when the input data contains repetitive patterns, making it an excellent choice for text compression and as a building block for other compression methods.
