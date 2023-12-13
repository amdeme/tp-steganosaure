import pytest
from steganosaure.stegano import encode_string, decode_bits

import numpy as np

def test_encodeString() -> None:
    np.testing.assert_array_equal(encode_string("ABC"), np.array([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]))

def test_decodeString() -> None:
    np.testing.assert_array_equal(decode_bits(np.array([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1])), "ABC")

def testcomplet() -> None:
    assert (decode_bits(encode_string("ABC")) == "ABC")
