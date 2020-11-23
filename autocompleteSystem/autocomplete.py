def autocomplete(s: str, queries: list) -> list:
    return [i for i in set(queries) if i.startswith(s)]
