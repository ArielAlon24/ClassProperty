# ClassProperty

Decorator for enhancing class methods with property-like behavior.

## Usage

```python
class A:
    @class_property
    def metadata(cls) -> str:
        return "a"
```
