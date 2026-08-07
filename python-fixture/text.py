def initials(name: str) -> str:
    """The first letter of each word in a name, uppercased and joined by dots."""
    return ".".join(word[0].upper() for word in name.split())


def truncate(text: str, limit: int) -> str:
    """Shorten text to at most `limit` characters, marking the cut with an ellipsis."""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."
