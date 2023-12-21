# ClassProperty

Decorator for enhancing class methods with property-like behavior.

## Usage

```python
from class_property import class_property


class A:
    @class_property
    def metadata(cls) -> str:
        return "a"
```
