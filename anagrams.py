def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    word1, word2 = word1.lower(), word2.lower()
    letters1 = sorted(char for char in word1 if word1.isalpha())
    letters2 = sorted(char for char in word2 if word2.isalpha())
    return letters1 == letters2
