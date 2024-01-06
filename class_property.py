from typing import TypeVar, Generic, Callable, Tuple
import inspect


T = TypeVar("T")


class _ClassProperty(property, Generic[T]):
    ARGUMENTS: Tuple[str] = ("cls",)

    def __init__(self, function: Callable[..., T]) -> None:
        super().__init__()
        if not self._is_validated(function):
            raise ValueError("Unexpected arguments.")
        self.function = function

    def _is_validated(self, function: Callable[..., T]) -> bool:
        return tuple(inspect.signature(function).parameters) == self.ARGUMENTS

    def __get__(self, _, owner=None) -> T:
        if owner:
            return self.function(owner)
        raise TypeError("Owner must not be None (unreachable).")


class_property = _ClassProperty
