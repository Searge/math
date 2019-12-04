def caesar(k, message):
    """The Caesar cipher used in Gravity Falls substitutes
    the original letter for the third letter before it.
    In the case for letters X, Y, and Z, one would have
    to cycle through to the beginning of the alphabet.
    """
    ciphertext = ''
    for symbol in message:
        if not symbol.isalpha():
            ciphertext += symbol
            continue
        char = ord(symbol) + k
        if ord('a') > char > ord('Z') or char > ord('z'):
            char -= 26
        ciphertext += chr(char)
    return ciphertext


def atbash(message):
    """Atbash ciphers are decoded by reversing the letters.
    For example, an A turns into a Z. """
    pass


def a1z25():
    """
    The A1Z26 cipher is a simple substitution cipher decoded
    by substituting the nᵗʰ letter of the alphabet
    for given number n.
    """
    pass


if __name__ == "__main__":
    pass
