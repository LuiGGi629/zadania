def get_ascii_codes(words):
    """Return a dictionary mapping the strings to ASCII codes."""
    codes = {}
    for word in words:
        codes[word] = [ord(char) for char in word]
    return codes
