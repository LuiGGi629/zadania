words = {
    "esta": "is",
    "la": "the",
    "en": "in",
    "rato": "rat",
    "el": "the",
    "casa": "house",
}


def transliterate(sentence):
    """Return a transliterated version of the given sentence."""
    transliterated = ""
    for word in sentence.split():
        transliterated += words[word] + " "
    return transliterated.rstrip()
