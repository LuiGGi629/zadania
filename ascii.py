def get_ascii_codes(words):
    """Return a dictionary mapping the strings to ASCII codes."""
    return {
        word: [ord(char) for char in word]
        for word in words
    }
