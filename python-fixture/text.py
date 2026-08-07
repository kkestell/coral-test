def initials(name: str) -> str:
    """The first letter of each word in a name, uppercased and joined by dots."""
    return ".".join(word[0].upper() for word in name.split())


def surname(name: str) -> str:
    """The last word of a name."""
    return name.split(" ")[-1]


def initial_and_surname(name: str) -> str:
    """A name as `A. Lovelace`."""
    return f"{name[0].upper()}. {surname(name)}"
