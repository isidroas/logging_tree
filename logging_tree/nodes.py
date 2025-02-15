"""Routine that explores the `logging` hierarchy and builds a `Node` tree."""

import logging


def _get_parent_name(name):
    """
    >>> _get_parent_name('a')
    ''
    >>> _get_parent_name('a.b')
    'a'
    >>> _get_parent_name('a.b.c')
    'a.b'
    """
    i = name.rfind('.', 0, len(name) - 1)  # same formula used in `logging`
    if i == -1:
        return ''
    else:
        return name[:i]


def tree():
    """Return a tree of tuples representing the logger layout.

    Each tuple looks like ``('logger-name', <Logger>, [...])`` where the
    third element is a list of zero or more child tuples that share the
    same layout.

    """
    root = ('', logging.root, [])
    nodes = {'': root}
    items = list(logging.root.manager.loggerDict.items())  # for Python 2 and 3
    items.sort()
    for name, logger in items:
        nodes[name] = node = (name, logger, [])
        _, _, parent_childs = nodes[_get_parent_name(name)]
        parent_childs.append(node)
    return root
