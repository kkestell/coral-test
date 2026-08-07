def initials(name: str) -> str:
    """The first letter of each word in a name, uppercased and joined by dots."""
    return ".".join(word[0].upper() for word in name.split())


def truncate(text: str, width: int) -> str:
    """Cut text down to `width` characters, ending with an ellipsis when it had to cut."""
    if len(text) <= width:
        return text
    return text[: width - 3] + "..."


def wrap(text: str, width: int) -> list[str]:
    """Break text into lines no longer than `width`, breaking only between words."""
    lines: list[str] = []
    current = ""
    for word in text.split():
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def columns(rows: list[list[str]]) -> str:
    """Lay rows out as a table, every column padded to its widest cell."""
    widths = [max(len(row[index]) for row in rows) for index in range(len(rows[0]))]
    return "\n".join(
        "  ".join(cell.ljust(width) for cell, width in zip(row, widths)) for row in rows
    )


def slugify(title: str) -> str:
    """A title reduced to lowercase words joined by hyphens."""
    kept = [character if character.isalnum() else " " for character in title]
    return "-".join("".join(kept).lower().split())
