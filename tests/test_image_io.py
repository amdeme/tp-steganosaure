import pytest
from steganosaure.stegano import load_image, save_image

def test_image() -> None:   
    #save_image(image: np.ndarray, image_path: pathlib.Path)
    #load_image(image_path: pathlib.Path) -> np.ndarray:
    save_image(load_image('image\museum.jpg'), 'image\museum_test.jpg)'
    assert load_image(image\save_image()) == load_image()

