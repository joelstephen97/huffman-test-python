import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, code="", huffman_codes={}):
    if node:
        if node.char is not None:
            huffman_codes[node.char] = code
        build_codes(node.left, code + "0", huffman_codes)
        build_codes(node.right, code + "1", huffman_codes)
    return huffman_codes

def compress(data):
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    huffman_codes = build_codes(root)
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, root

def decompress(encoded_data, root):
    decoded_data = []
    node = root
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if node.char is not None:
            decoded_data.append(node.char)
            node = root
    
    return ''.join(decoded_data)


data = """
This is the end
Hold your breath and count to ten
Feel the earth move and then
Hear my heart burst again
For this is the end
I've drowned and dreamt this moment
So overdue, I owe them
Swept away, I'm stolen
Let the sky fall
When it crumbles
We will stand tall
Face it all together
Let the sky fall
When it crumbles
We will stand tall
Face it all together at Skyfall
At Skyfall
Skyfall is where we start
A thousand miles and poles apart
Where worlds collide and days are dark
You may have my number, you can take my name
But you'll never have my heart
Let the sky fall (let the sky fall)
When it crumbles (when it crumbles)
We will stand tall (we will stand tall)
Face it all together
Let the sky fall (let the sky fall)
When it crumbles (when it crumbles)
We will stand tall (we will stand tall)
Face it all together at Skyfall
(Let the sky fall)
(When it crumbles)
(We will stand tall)
(Let the sky fall)
(When it crumbles)
(We will stand tall)
Where you go, I go
What you see, I see
I know I'd never be me
Without the security
Of your loving arms
Keeping me from harm
Put your hand in my hand
And we'll stand
Let the sky fall (let the sky fall)
When it crumbles (when it crumbles)
We will stand tall (we will stand tall)
Face it all together
Let the sky fall (let the sky fall)
When it crumbles (when it crumbles)
We will stand tall (we will stand tall)
Face it all together at Skyfall
Let the sky fall
We will stand tall
At Skyfall
Ooh
"""
print("Original Data:", data)

compressed_data, tree = compress(data)
print("Compressed Data:", compressed_data)

decompressed_data = decompress(compressed_data, tree)
print("Decompressed Data:", decompressed_data)

original_size = len(data) * 8 
encoded_size = len(compressed_data)  
decoded_size = len(decompressed_data) * 8 

print(f"Size of Original Data: {original_size} bits ({len(data)} characters)")
print(f"Size of Encoded Data: {encoded_size} bits")
print(f"Size of Decoded Data: {decoded_size} bits ({len(decompressed_data)} characters)")