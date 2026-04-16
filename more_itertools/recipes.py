"""Minimal recipe helpers required by the local copied more_itertools.more."""

from collections import deque
from itertools import chain, combinations, islice, tee

_marker = object()


class UnequalIterablesError(ValueError):
    """Raised when iterables are unexpectedly unequal."""


def _zip_equal(*iterables):
    return zip(*iterables)


def consume(iterator, n=None):
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


def flatten(iterable):
    return chain.from_iterable(iterable)


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def powerset(iterable):
    items = list(iterable)
    return chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))


def take(n, iterable):
    return list(islice(iterable, n))


def unique_everseen(iterable, key=None):
    seen = set()
    for item in iterable:
        marker = item if key is None else key(item)
        if marker in seen:
            continue
        seen.add(marker)
        yield item


def all_equal(iterable, key=None):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return True

    first_marker = first if key is None else key(first)
    for item in iterator:
        marker = item if key is None else key(item)
        if marker != first_marker:
            return False
    return True


def batched(iterable, n):
    if n < 1:
        raise ValueError("n must be at least 1")

    iterator = iter(iterable)
    while True:
        batch = tuple(islice(iterator, n))
        if not batch:
            break
        yield batch