import random
import typing as tp


def is_prime(N: int) -> bool:
    """
    Tests to see if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if N == 1:
        return False

    prime = True
    for i in range(2, int(N ** (1 / 2)) + 1):
        if N % i == 0:
            prime = False
            break
    return prime
    pass


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if (a == 0 or b == 0):
        return max(a, b)

    a, b = max(a, b), min(a, b)
    r1 = b
    r2 = a % b

    while r2 > 0:
        r1 = r1 % r2
        r1, r2 = r2, r1
    return r1
    pass


def multiplicative_inverse(e: int, phi: int) -> int:

    a = phi
    b = e
    A = []
    B = []
    A_mod_B = []
    A_div_B = []
    X = []
    Y = []

    A.append(a)
    B.append(b)
    A_mod_B.append(a % b)
    A_div_B.append(a // b)
    a, b = b, a % b

    while A_mod_B[-1] != 0:
        A.append(a)
        B.append(b)
        A_mod_B.append(a % b)
        A_div_B.append(a // b)
        a, b = b, a % b

    X.append(0)
    Y.append(1)

    print(A)
    print(B)
    print(A_mod_B)
    print(A_div_B)


    n = len(A)
    for i in range(n-1, -1, -1):
        x = Y[-1]
        y = X[-1] - Y[-1] * A_div_B[i]
        X.append(x)
        Y.append(y)

    return Y[-1] % phi

print(multiplicative_inverse(7, 40))


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = pq
    phi = (p-1)(q-1)
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
