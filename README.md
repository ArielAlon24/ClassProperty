# ClassProperty

Decorator for enhancing class methods with property-like behavior.

## Usage

To utilize `class_property`, decorate a class method and pass `cls` as an argument. This allows the method to be accessed like a property, using either the class itself or its instances.

```python
from class_property import class_property

class A:
    @class_property
    def metadata(cls) -> str:
        return "test123"

# Access 'metadata' using the class:
print(A.metadata)  # Outputs: test123

# Access 'metadata' using an instance of the class:
a = A()
print(a.metadata)  # Outputs: test123
```