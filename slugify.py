"""Turning a title into a URL slug."""

import re

SEPARATORS = re.compile(r"[^a-z0-9]+")


def slugify(title: str) -> str:
    """A lowercase, hyphen-separated form of the title, safe in a URL path.

    Runs of anything that is not a letter or a digit become one hyphen, and leading and
    trailing hyphens are trimmed. An empty title, or one with nothing but punctuation,
    gives an empty string.
    """
    return SEPARATORS.sub("-", title.lower()).strip("-")
