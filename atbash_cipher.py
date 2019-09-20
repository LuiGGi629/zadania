from string import ascii_lowercase as letters

atbash = dict(zip(letters, reversed(letters)))


def decode(string):
    """Return string of each character decoded."""
    return "".join(
        atbash.get(char, char)
        for char in string.lower()
        if char.isalnum()
    )
