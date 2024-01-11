from typing import TypeVar, Generic, Callable, Tuple
import inspect


T = TypeVar("T")


class _ClassProperty(Generic[T], property):
    PARAMETERS: Tuple[str] = ("cls",)

    def __init__(self, method: Callable[..., T]) -> None:
        super().__init__()
        if not tuple(inspect.signature(method).parameters) == self.PARAMETERS:
            raise ValueError(f"Incorrect arguments, expected: {self.PARAMETERS}.")
        self.method = method

    def __get__(self, _, owner=None) -> T:
        if owner:
            return self.method(owner)
        raise TypeError("Owner must not be None (unreachable).")


class_property = _ClassProperty
