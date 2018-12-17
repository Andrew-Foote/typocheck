import string
import typing as t

def iterwords(s: str) -> t.Iterator[str]:
    """Iterate over the strings of consective ASCII letters of the same case
    in ``s``.

    >>> tuple(iterwords('ada -b12CANGOslot.froarr'))
    ('ada', 'b', 'CANGO', 'slot', 'froarr')
    """
    word: List[str] = []
    word_is_uppercase: bool = False

    def flush() -> t.Iterator[str]:
        if word:
            yield ''.join(word)
            word.clear()

    for c in s:
        if word_is_uppercase:
            if c in string.ascii_uppercase:
                word.append(c)
            else:
                yield from flush()
                if c in string.ascii_lowercase:
                    word.append(c)
                    word_is_uppercase = False
        else:
            if c in string.ascii_lowercase:
                word.append(c)
            else:
                yield from flush()
                if c in string.ascii_uppercase:
                    word.append(c)
                    word_is_uppercase = True

    yield from flush()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
