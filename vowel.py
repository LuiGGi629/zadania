def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    vowel_names = []
    for name in names:
        if name[0].lower() in "aeiou":
            vowel_names.append(name)
    return vowel_names
