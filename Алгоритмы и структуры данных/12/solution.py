from PIL import Image
import numpy as np
from collections import defaultdict

def load_image(image_path):
    image = Image.open(image_path).convert("L")
    return np.array(image)

class ColorTree:
    def __init__(self):
        self.tree = defaultdict(int)

    def add_pixel(self, intensity):
        self.tree[intensity] += 1

    def build_tree(self, pixel_values):
        for value in pixel_values:
            self.add_pixel(value)

    def compress(self, pixel_values):
        compressed = []
        for value in pixel_values:
            compressed.append(self.tree.get(value, 0))
        return compressed

    def decompress(self, compressed_values, unique_values):
        decompressed = []
        idx = 0
        for _ in compressed_values:
            decompressed.append(unique_values[idx])
            idx += 1
        return decompressed

def compress_image(image_array):
    unique_values = np.unique(image_array)
    color_tree = ColorTree()
    color_tree.build_tree(image_array.flatten())
    compressed_image = color_tree.compress(image_array.flatten())
    return compressed_image, unique_values

def decompress_image(compressed_image, unique_values, shape):
    color_tree = ColorTree()
    decompressed_values = color_tree.decompress(compressed_image, unique_values)
    decompressed_image = np.array(decompressed_values).reshape(shape)
    return decompressed_image

def main(image_path):
    image = load_image(image_path)
    
    compressed_image, unique_values = compress_image(image)
    decompressed_image = decompress_image(compressed_image, unique_values, image.shape)

    result_image = Image.fromarray(decompressed_image.astype(np.uint8))
    result_image.show()

    result_image.save("restored_image.bmp")

if __name__ == "__main__":
    main("./test_image.bmp")
