"""
This module contains helper classes used in tests
"""


class LessThanableElement(object):
    """
    Wraps any object and forwards invocations to __lt__ to it
    """
    def __init__(self, val):
        self._val = val

    @property
    def val(self):
        return self._val

    def __lt__(self, other):
        if not isinstance(other, LessThanableElement):
            raise TypeError("Can't compare to object of type %s" % type(other))

        return self.val < other.val


class SubscriptableClassWithoutLen(object):
    """
    Dummy object that implement __getitem__, used in tests to pass the __getitem__ check only
    """
    def __getitem__(self, item):
        pass


class UnscubscriptableClassWithLen(object):
    """
    Dummy object that implement __getitem__, used in tests to pass the __len__ check only
    """
    def __len__(self):
        return 0
