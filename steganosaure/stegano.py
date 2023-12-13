import numpy as np
import skimage
import pathlib


def encode_string(string: str) -> np.ndarray:
    # Conversion en représentation binaire
    binary_list = [format(ord(char), '08b') for char in string]
    # Concatenation de la chaîne de bits
    binary_string = ''.join(binary_list)
    # Création du  tableau NumPy à partir de la chaîne de bits
    numpy_array = np.array([int(bit) for bit in binary_string], dtype=np.uint8)
    return numpy_array

def decode_bits(bits: np.ndarray) -> str :
    #conversion numpy.Array => string de bit
    unpack_binary_string = np.packbits(bits)
    return bytes(unpack_binary_string).decode('utf-8')


#Partie 2
def load_image(image_path: pathlib.Path) -> np.ndarray:
    # Charger l'image à l'aide de la fonction imread de scikit-image
    image = io.imread(image_path)
    # Convertir l'image en tableau NumPy d'entiers sur 8 bits
    image_8bits = util.img_as_ubyte(image)
    return image_8bits

def save_image(image: np.ndarray, image_path: pathlib.Path) -> None:
    """
    Sauvegarde un tableau NumPy en tant qu'image PNG.

    Parameters:
    - image (numpy.ndarray): Le tableau NumPy représentant l'image.
    - image_path (str): Le chemin de sauvegarde de l'image.
    """
    io.imsave(image_path, image)