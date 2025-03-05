import random
from typing import List, Tuple


# Function to generate a random polynomial
def generate_coefficients(secret: int, threshold: int) -> List[int]:
    coefficients = [secret]
    for _ in range(threshold - 1):
        coefficients.append(random.randint(1, 256))
    return coefficients


# Function to create shares
def create_shares(secret, total_shares: int, threshold: int):
    
    secret_decimal = int.from_bytes(secret, 'big')
    coefficients = generate_coefficients(secret_decimal, threshold)
    shares = []
    for x in range(1, total_shares + 1):
        y = sum(coeff * (x**exp) for exp, coeff in enumerate(coefficients))
        shares.append((x, hex(y)[2:]))
    return shares


# Function to reconstruct the secret
def reconstruct_secret(shares: List[Tuple[int, str]], threshold: int) -> int:
    def _lagrange_interpolation(x: int, x_s: List[int], y_s: List[str]) -> int:
        y_s = [int(y, 16) for y in y_s]
        def _basis(j: int) -> int:
            num = 1
            den = 1
            for m in range(len(x_s)):
                if m != j:
                    num *= x - x_s[m]
                    den *= x_s[j] - x_s[m]
            return num // den

        result = 0
        for j in range(len(y_s)):
            result += y_s[j] * _basis(j)
        return result

    x_s, y_s = zip(*shares)
    secret = _lagrange_interpolation(0, x_s, y_s)
    array = hex(secret)[2:]
    return bytes.fromhex(array)


# Example usage
if __name__ == "__main__":
    secret = b'\xbfe\x94C\x08\xa5Fk7\x8eC\x82\x8b\x11a\x0f(\x04j\xd2A\x15\x80\x03\xf6\xa0E\x90\xea\\x/'# Example key
    total_shares = 5
    threshold = 3

    shares = create_shares(secret, total_shares, threshold)
    print("Shares:", shares)

    selected_shares = shares[:threshold]
    recovered_secret = reconstruct_secret(selected_shares, threshold)
    print("Recovered Secret:", recovered_secret)
    
    assert secret == recovered_secret
    print("Secret successfully recovered!")