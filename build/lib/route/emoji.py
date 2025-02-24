import re
from typing import Tuple

def is_emoji(char: str) -> bool:
    """Returns True if the character is an emoji."""
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F]"  # Emoticons
        "|[\U0001F300-\U0001F5FF]"  # Symbols & pictographs
        "|[\U0001F680-\U0001F6FF]"  # Transport & map symbols
        "|[\U0001F700-\U0001F77F]"  # Alchemical symbols
        "|[\U0001F780-\U0001F7FF]"  # Geometric shapes
        "|[\U0001F800-\U0001F8FF]"  # Supplemental symbols and pictographs
        "|[\U0001F900-\U0001F9FF]"  # Supplemental symbols and pictographs (second range)
        "|[\U0001FA00-\U0001FA6F]"  # Chess symbols, symbols for text, emoticons
        "|[\U0001FA70-\U0001FAFF]"  # More symbols and pictographs
        "|[\U00002702-\U000027B0]"  # Dingbats
        "|[\U000024C2-\U0001F251]"  # Enclosed characters
        "+", flags=re.UNICODE)

    return bool(emoji_pattern.fullmatch(char))

def pad_emoji_in_string(string: str, padding: Tuple[str, str]) -> str:
    """
    """
    if len(string) == 0:
        return string
    else:
        if is_emoji(string[0]):
            string = padding[0] + string
        if is_emoji(string[-1]):
            string = string + padding[1]
        return string
