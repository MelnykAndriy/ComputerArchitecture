__author__ = 'mandriy'

from threading import Lock


_lock_groups = {}


def make_thread_safe(group):
    if group not in _lock_groups:
        _lock_groups[group] = Lock()
    group_mutex = _lock_groups[group]

    def thread_safe_decorator(func):
        def thread_safe_func(*args, **kwargs):
            try:
                group_mutex.acquire()
                return func(*args, **kwargs)
            finally:
                group_mutex.release()

        return thread_safe_func

    return thread_safe_decorator
