import re
from re import Match


def email(address: str) -> Match | None:
    regex = re.compile(r'^.+@.+\..+$')
    match = regex.match(address)
    return match
