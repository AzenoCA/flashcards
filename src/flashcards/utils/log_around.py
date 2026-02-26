from __future__ import annotations

import inspect
import logging
from functools import wraps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def log_around[**P, R](fn: Callable[P, R]) -> Callable[P, R]:
    """Decorator that provides structured debug-level logging around a callable.

    This decorator logs:
    - The fully qualified function name before execution,
    - All bound input arguments (including default values),
    - The returned value after successful execution.

    Logging is performed using a module-level logger derived from the wrapped
    function's ``__module__`` attribute. Function metadata is preserved via
    ``functools.wraps``.

    Parameters
    ----------
    fn : Callable[P, R]
        The target callable to be wrapped. Supports arbitrary positional
        and keyword arguments via ParamSpec.

    Returns:
    -------
    Callable[P, R]
        A wrapped callable with identical signature and return type that
        emits structured debug logs before and after execution.

    Logging Details
    ---------------
    - Log level: DEBUG
    - Logger name: module of the wrapped function
    - Structured fields:
        * "params": dictionary of argument names to repr(value)
        * "output": repr(return_value)

    Notes:
    -----
    - Argument binding is performed using ``inspect.signature`` to ensure
      accurate parameter mapping, including default values.
    - All values are logged using ``repr()`` to provide unambiguous
      developer-oriented representations.
    - This decorator does not handle or log exceptions; exceptions propagate
      unchanged to the caller.
    - Excessive use in performance-critical paths may introduce overhead
      due to signature binding and object representation.

    Example:
    -------
    >>> @log_around
    ... def add(x: int, y: int) -> int:
    ...     return x + y
    ...
    >>> add(2, 3)
    # DEBUG: Calling add
    # DEBUG: Returned add

    """
    signature = inspect.signature(fn)
    callable_name = fn.__qualname__  # ty: ignore[unresolved-attribute]
    func_logger = logging.getLogger(fn.__module__)

    @wraps(wrapped=fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()
        params = {name: repr(value) for name, value in bound.arguments.items()}

        func_logger.debug("Calling %s", callable_name, extra={"params": params})

        result = fn(*args, **kwargs)

        func_logger.debug("Returned %s", callable_name, extra={"output": repr(result)})
        return result

    return wrapper
