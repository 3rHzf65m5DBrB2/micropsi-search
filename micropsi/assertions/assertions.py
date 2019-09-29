import logging
__logger = logging.getLogger(__name__)


def ensure_not_none(obj, error_msg):
    check(obj is not None, error_msg, True)


def ensure_subscriptable(obj, error_msg):
    check(hasattr(obj, "__getitem__"), error_msg, True)


def ensure_has_length(obj, error_msg):
    check(hasattr(obj, "__len__"), error_msg, True)


def check(predicate, error_msg, fail=False):
    if not predicate:
        if not fail:
            __logger.warning(error_msg)
            return False
        raise AssertionError

    return True
