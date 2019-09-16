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
    return " ".join(
            words[word]
            for word in sentence.split()
    )
