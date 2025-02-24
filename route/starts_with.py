def starts_with(string: str, starts_with_set: set[str]) -> bool:
    for starts_with in starts_with_set:
        if string.startswith(starts_with):
            return True
    return False

def ends_with(string: str, ends_with_set: set[str]) -> bool:
    for ends_with in ends_with_set:
        if string.endswith(ends_with):
            return True
    return False