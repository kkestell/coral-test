TITLES = {"dr", "mr", "mrs", "ms", "prof"}


def initials(name: str) -> str:
    """The first letter of each word in a name, uppercased and joined by dots.

    A leading title is dropped: "Dr Ada Lovelace" gives "A.L".
    """
    words = name.split()
    if words[0].rstrip(".").lower() in TITLES:
        words = words[1:]
    return ".".join(word[0].upper() for word in words)
