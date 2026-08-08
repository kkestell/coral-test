def initials(name: str) -> str:
    """The first letter of each word in a name, uppercased and joined by dots."""
    return ".".join(word[0].upper() for word in name.split())


def shortened(text: str, limit: int) -> str:
    """`text` cut to at most `limit` characters, ending in an ellipsis when it was cut."""
    if len(text) <= limit:
        return text
    return text[:limit] + "…"
