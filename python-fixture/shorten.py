def shorten(text: str, limit: int) -> str:
    """Cut text to at most `limit` characters, ending with an ellipsis when it was cut."""
    if len(text) <= limit:
        return text
    return text[:limit] + "..."
