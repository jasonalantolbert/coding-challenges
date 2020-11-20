import itertools

import regex as re


def find_substring(s: str, words: list[str]) -> list[int]:
    regex_str = ""
    for arrangement in itertools.permutations(words, r=len(words)):
        regex_str += f"{''.join(arrangement)}|"

    regex = re.compile(regex_str.rstrip("|"))

    matches = []

    for match in re.finditer(regex, s, overlapped=True):
        matches.append(match.span(0)[0])

    return matches

