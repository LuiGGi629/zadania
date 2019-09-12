def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [
        name
        for name in names
        if name[0].lower() in "aeiou"
    ]
