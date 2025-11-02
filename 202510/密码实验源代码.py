from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import random

def bytes_to_bits(b):
    return ''.join(f'{byte:08b}' for byte in b)

def bit_diff(a, b):
    return sum(x != y for x, y in zip(bytes_to_bits(a), bytes_to_bits(b)))

def flip_one_bit(data):
    bit_index = random.randint(0, len(data) * 8 - 1)
    byte_index, bit_in_byte = divmod(bit_index, 8)
    new_data = bytearray(data)
    new_data[byte_index] ^= (1 << bit_in_byte)
    return bytes(new_data)


def test_fixed_key(num_tests=100):
    key = bytes([0] * 16)
    cipher = AES.new(key, AES.MODE_ECB)
    total_diff = 0

    for _ in range(num_tests):
        m = get_random_bytes(16)
        m_prime = flip_one_bit(m)
        c1 = cipher.encrypt(m)
        c2 = cipher.encrypt(m_prime)
        total_diff += bit_diff(c1, c2)

    avg_diff = total_diff / num_tests
    return avg_diff / 128


def test_fixed_plaintext(num_tests=100):
    plaintext = bytes([0] * 16)
    total_diff = 0

    for _ in range(num_tests):
        k = get_random_bytes(16)
        k_prime = flip_one_bit(k)
        c1 = AES.new(k, AES.MODE_ECB).encrypt(plaintext)
        c2 = AES.new(k_prime, AES.MODE_ECB).encrypt(plaintext)
        total_diff += bit_diff(c1, c2)

    avg_diff = total_diff / num_tests
    return avg_diff / 128


if __name__ == "__main__":
    result1 = test_fixed_key()
    result2 = test_fixed_plaintext()
    print(f"固定密钥改变明文的平均不同位比例: {result1 * 100:.2f}%")
    print(f"固定明文改变密钥的平均不同位比例: {result2 * 100:.2f}%")