def initials(name: str) -> str:
    """The first letter of each word in a name, uppercased and joined by dots."""
    return ".".join(word[0].upper() for word in name.split())
