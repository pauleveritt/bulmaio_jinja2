from pathlib import Path

SEP = "/"


# Taken from Sphinx
def relative_uri(base, to):
    # type: (unicode, unicode) -> unicode
    """Return a relative URL from ``base`` to ``to``."""
    if to.startswith(SEP):
        return to
    b2 = base.split(SEP)
    t2 = to.split(SEP)
    # remove common segments (except the last segment)
    for x, y in zip(b2[:-1], t2[:-1]):
        if x != y:
            break
        b2.pop(0)
        t2.pop(0)
    if b2 == t2:
        # Special case: relative_uri('f/index.html','f/index.html')
        # returns '', not 'index.html'
        return ''
    if len(b2) == 1 and t2 == ['']:
        # Special case: relative_uri('f/index.html','f/') should
        # return './', not ''
        return '.' + SEP
    return ('..' + SEP) * (len(b2) - 1) + SEP.join(t2)


def static_path(static_dirname, docname, other):
    full_other = Path(static_dirname, other)
    target = relative_uri(docname, str(full_other))
    return target
